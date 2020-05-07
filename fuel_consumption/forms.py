from django import forms
from .models import FuelSupply
from tempus_dominus.widgets import DateTimePicker
from django.utils import timezone


class FuelSupplyForm(forms.ModelForm):
    class Meta:
        model = FuelSupply
        fields = ['date', 'price', 'amount', 'mileage']
        labels = {
            'date': 'Data',
            'price': 'Preço do combustível',
            'amount': 'Valor abastecido',
            'mileage': 'Quilometragem atual',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['date'] = forms.DateTimeField(widget = DateTimePicker(options={'useCurrent': True, 'locale':'pt-br', 'format':'DD/MM/YYYY HH:mm:ss'}),
                                               # input_formats=['%d/%m/%Y %H:%M:%S'], label='Data')
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

        # for field in self.fields.keys():
        #     attr_class = ''
        #     if self.fields[field].widget.attrs.get('class'):
        #         attr_class = str(self.fields[field].widget.attrs.get('class'))
        #     self.fields[field].widget.attrs.update({'class':attr_class + ' col-lg-5 col-md-8 col-sm-10'})
