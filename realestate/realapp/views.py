
from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.views import View
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes, force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate,login,logout
from .models import Contact
# Create your views here.
def handlelogin(request):
    
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)
    if myuser is not None:
        login(request,myuser)
        messages.success(request,"Login successful")
        return render(request,"index.html")
    else:
        messages.error(request,"invalid Credentials")
        return redirect(request,'login')
    return render(request,'login.html')


def handlesignup(request):

    if request.method=="POST":
        uname=request.POST['username']
        password1=request.POST['pass1']
        confpass=request.POST['pass2']
        email=request.POST['email']


        if password1!=confpass:
            messages.warning(request,"passwords dint match!")
            return render(request,'signup.html')
        try:
            if User.objects.get(email=email):
                messages.info(request,"Email already exists!")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        
        user=User.objects.create_user(uname,email,password1)
        user.is_active=False
        user.save()
        email_subject="Please Activate Your Account."
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127:0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })

        email_message= EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()
        messages.success(request,"click the link below to activate your account")
        
        return redirect('login')



    return render(request,'signup.html')


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            
            messages.info(request,"Account activated succefully")
            return redirect('/login')
        return render(request,'activatefail.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        mesage=request.POST.get('message')
        
        query=Contact(name=name,email=email,subject=subject,mesage=mesage)
        query.save()
        
        messages.success(request,"Thank you For contacting us we'll get back to you soon...")
        return redirect('contact')
        
    
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def logout(request):
    return render(request,'login.html')


