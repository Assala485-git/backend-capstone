from django.db import models

# Create your models her

class Booking(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    guests=models.IntegerField()
    booking_date=models.DateTimeField()

class MenuItem(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    inventory=models.IntegerField()