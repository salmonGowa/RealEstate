#from base64 import urlsafe_b64encode

from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import TokenGenerator,generate_token
from django.utils.encoding import force_bytes
# Create your views here.
def handlelogin(request):
    
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
            if User.objects.get(username=email):
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



    return render(request,'signup.html')



def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def logout(request):
    return render(request,'login.html')
