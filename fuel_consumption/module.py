from .models import FuelSupply
from django.core.exceptions import ObjectDoesNotExist

def get_latest_average_consumption():
    try:
        current_fuel_supply = FuelSupply.objects.latest()
        last_fuel_supply = FuelSupply.objects.exclude(date=current_fuel_supply.date).latest()
        liters_quantity = current_fuel_supply.amount / current_fuel_supply.price
        travelled_distance = current_fuel_supply.mileage - last_fuel_supply.mileage
        average_consumption = travelled_distance / liters_quantity
    except ObjectDoesNotExist:
        return 0
    return average_consumption
