from django.shortcuts import render
from django.views import generic
from .models import FuelSupply
from .forms import FuelSupplyForm

class FuelSupplyCreate(generic.CreateView):
    form_class = FuelSupplyForm
    template_name = 'fuel_consumption/fuelsupply_form.html'

    def form_invalid(self, form):
        print('INVALIDO: ', form.fields)
        return super().form_invalid(form)

    def form_valid(self, form):
        print('VALIDO: ', form.fields)
        return super().form_valid(form)

class FuelSupplyList(generic.ListView):
    model = FuelSupply
    template_name = 'fuel_consumption/fuelsupply_list.html'
