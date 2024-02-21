from django.shortcuts import render

# Create your views here.
def handlelogin(request):
    return render(request,'login.html')
def handlesignup(request):
    return render(request,'signup.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')
