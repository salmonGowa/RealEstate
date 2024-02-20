from django.shortcuts import render

# Create your views here.
def handlelogin(request):
    return render(request,'login.html')