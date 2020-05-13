from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.brand + ' - ' + self.model

class FuelSupply(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(null=False, default=timezone.now)
    price = models.FloatField(null=False)
    amount = models.FloatField(null=False)
    mileage = models.IntegerField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        get_latest_by = 'date'

class FuelSupplyUserPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view_all_vehicles_in_home = models.BooleanField(default=False)
    default_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
