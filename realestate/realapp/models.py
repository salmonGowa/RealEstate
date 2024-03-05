from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=50)
    mesage=models.TextField(max_length=150)


class Houses(models.Model):
    house_id=models.AutoField
   
    bedrooms=models.IntegerField()
    location=models.CharField(max_length=50)
    sizr_sq_feet=models.CharField(max_length=50)
    
    