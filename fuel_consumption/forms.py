from django import forms
from .models import FuelSupply
from tempus_dominus.widgets import DateTimePicker
from django.utils import timezone
from django.contrib.auth import get_user_model


class FuelSupplyForm(forms.ModelForm):
    class Meta:
        model = FuelSupply
        fields = ['vehicle','date', 'price', 'amount', 'mileage']
        labels = {
            'vehicle': 'Veículo',
            'date': 'Data',
            'price': 'Preço do combustível',
            'amount': 'Valor abastecido',
            'mileage': 'Quilometragem atual',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial['vehicle'] = 1
        self.fields['date'].widget.attrs['readonly'] = True
        self.fields['price'].widget = forms.TextInput(attrs={
            'type':'text',
            'class':'text-left',
            'data-inputmask':"'alias': 'numeric', 'groupSeparator': ',', 'autoGroup': true, 'digits': 2, 'digitsOptional': false, 'positionCaretOnClick': 'radixFocus', 'placeholder': '0'"
        })
        self.fields['amount'].widget = forms.TextInput(attrs={
            'type':'text',
            'class':'text-left',
            'data-inputmask':"'alias': 'numeric', 'groupSeparator': ',', 'autoGroup': true, 'digits': 2, 'digitsOptional': false, 'positionCaretOnClick': 'radixFocus', 'placeholder': '0'"
        })
