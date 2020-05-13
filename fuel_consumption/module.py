from .models import FuelSupply, Vehicle, FuelSupplyUserPreferences
from django.core.exceptions import ObjectDoesNotExist

def get_latest_average_consumption(user_param):
    vehicle_list = []
    vehicle_list_aux = []
    try:
        try:
            user_preferences = FuelSupplyUserPreferences.objects.get(user=user_param)
            if not user_preferences.view_all_vehicles_in_home:
                vehicle_list_aux = [user_preferences.default_vehicle]
            else:
                vehicle_list_aux = Vehicle.objects.all()
        except ObjectDoesNotExist:
            vehicle_list_aux = Vehicle.objects.all()
        for vehicle in vehicle_list_aux:
            current_fuel_supply = FuelSupply.objects.filter(vehicle=vehicle).latest()
            last_fuel_supply = FuelSupply.objects.filter(vehicle=vehicle).exclude(date=current_fuel_supply.date).latest()
            liters_quantity = current_fuel_supply.amount / current_fuel_supply.price
            travelled_distance = current_fuel_supply.mileage - last_fuel_supply.mileage
            average_consumption = travelled_distance / liters_quantity
            vehicle_list.append({'vehicle':vehicle, 'average_consumption':average_consumption})
    except ObjectDoesNotExist:
        return vehicle_list
    return vehicle_list

def get_user_preferences(user):
    try:
        user_preferences = FuelSupplyUserPreferences.objects.get(user=user)
        return user_preferences
    except ObjectDoesNotExist:
        return None
