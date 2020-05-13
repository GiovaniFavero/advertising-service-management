from django.views.generic import TemplateView
from fuel_consumption.models import FuelSupply
from fuel_consumption import module
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
User = get_user_model()

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle_list'] = module.get_latest_average_consumption(self.request.user)
        return context
