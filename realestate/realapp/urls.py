from django.urls import path
from realapp import views

urlpatterns = [

    path('',views.index,name="index"),
    path('handlelogin',views.handlelogin,name="handlelogin"),
    path('handlesignup',views.handlesignup,name="handlesignup"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('logout',views.logout,name="logout"),
    path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name='activate')
    ]
