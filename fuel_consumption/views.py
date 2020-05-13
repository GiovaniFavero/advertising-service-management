from django.views import generic
from .models import FuelSupply, FuelSupplyUserPreferences
from .forms import FuelSupplyForm
from . import module as fuel_module
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist

class FuelSupplyCreate(LoginRequiredMixin, generic.CreateView):
    form_class = FuelSupplyForm
    template_name = 'fuel_consumption/fuelsupply_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class FuelSupplyList(LoginRequiredMixin, generic.ListView):
    model = FuelSupply
    template_name = 'fuel_consumption/fuelsupply_list.html'
    def get_queryset(self):
        user_preferences = fuel_module.get_user_preferences(self.request.user)
        if user_preferences is None or not user_preferences.view_all_vehicles_in_home:
            return FuelSupply.objects.all()
        else:
            return FuelSupply.objects.filter(vehicle=user_preferences.default_vehicle)
