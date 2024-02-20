from django.urls import path
from .import views

urlpatterns = [
    path('handlelogin',views.handlelogin,name="handlelogin"),
    
]
