from django.db import models

# Create your models here.

class Customer(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname= models.CharField(max_length=50)
    Mobile = models.CharField(max_length=10)
    Email = models.EmailField()