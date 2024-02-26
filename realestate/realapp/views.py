from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User

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
            return render(request,'signup.html')
        try:
            if User.objects.get(username=email):
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        
        user=User.objects.create_user(uname,email,password1)
        user.save()



    return render(request,'signup.html')



def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
def logout(request):
    return render(request,'login.html')
