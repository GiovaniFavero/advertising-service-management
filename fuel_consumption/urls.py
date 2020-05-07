from django.urls import path
from .views import FuelSupplyCreate, FuelSupplyList

app_name = 'fuel_consumption'

urlpatterns = [
    path('fuel', FuelSupplyCreate.as_view(), name='fuel'),
    path('fuel_list', FuelSupplyList.as_view(), name='fuel_list'),
]
