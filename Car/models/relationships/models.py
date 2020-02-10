from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10)
     
    def __str__(self):
        return self.name

class Mechanics(models.Model):
    name = models.CharField(max_length=10)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Carparts(models.Model):
    name = models.CharField(max_length=10)
    cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.name 

class Engine(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=10)
    engine = models.OneToOneField(Engine, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Accounting(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
     
class Customers(models.Model):
    name = models.CharField(max_length=10)
    Accounting = models.ForeignKey(Accounting, on_delete=models.CASCADE)

    def __str__(self):
        return self.name