from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    is_customer = models.IntegerField(default=False) # 1 -> user   , 2-> mall , 3-> staff


  


class ParkingSlot(models.Model):
    mall=models.ForeignKey(User, on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=10, unique=True)
    is_reserved = models.BooleanField(default=False)
    vehicle_type = models.CharField(max_length=20, choices=[('Car', 'Car'), ('Bike', 'Bike')])
    location = models.IntegerField()
    is_occupied = models.IntegerField(default=0) # 0 -> Free   , 1-> booked , 2-> alotted ,3 -> paid

class Rate(models.Model):
    mall=models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=20, choices=[('Car', 'Car'), ('Bike', 'Bike')])
    rate_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    rate_per_day = models.DecimalField(max_digits=6, decimal_places=2)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="user")    
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
   

class Location(models.Model):
    location=models.CharField(max_length=100)

class Mall(models.Model):
    mall = models.ForeignKey(User, on_delete=models.CASCADE , related_name="mall")    
    loc_id = models.ForeignKey(Location, on_delete=models.CASCADE)    
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    # lat=models.CharField(max_length=20)
    # lon=models.CharField(max_length=20)
    
class Staff(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="staff") 
    mall = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="mall_staff") 