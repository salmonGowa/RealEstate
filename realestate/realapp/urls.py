from django.urls import path
from realapp import views

urlpatterns = [
    path('handlelogin',views.handlelogin,name="handlelogin"),
    path('handlesignup',views.handlesignup,name='handlesignup'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('home',views.home,name='home'),
]
