from django.contrib import admin
from fuel_consumption.models import FuelSupply, Vehicle, FuelSupplyUserPreferences
# Register your models here.
admin.site.register(FuelSupply)
admin.site.register(Vehicle)
admin.site.register(FuelSupplyUserPreferences)
