from django.forms import Widget


class CurrencyInput(Widget):

    def get_context(name, value, attrs, test):
        attrs = {
            'class': 'form-control col-sm-4'
        }
