from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    location= models.CharField(max_length=255)
    message = models.CharField(max_length=255)
   

# Create your models here.
