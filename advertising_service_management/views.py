from django.views.generic import TemplateView
from fuel_consumption.models import FuelSupply
from fuel_consumption import module

class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['average_consumption'] = module.get_latest_average_consumption()
        return context
