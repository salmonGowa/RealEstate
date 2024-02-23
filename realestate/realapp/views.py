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
            return HttpResponse("Password Dont Match")
        
        user=User.objects.create_user(uname,password1,email)
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
