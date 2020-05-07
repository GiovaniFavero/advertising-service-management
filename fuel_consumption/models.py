from django.db import models
from django.urls import reverse
from django.utils import timezone
from djmoney.models.fields import MoneyField


class FuelSupply(models.Model):
    date = models.DateTimeField(null=False, default=timezone.now)
    price = models.FloatField(null=False)
    amount = models.FloatField(null=False)
    mileage = models.IntegerField(null=False)

    def get_absolute_url(self):
        return reverse('index')

    class Meta:
        get_latest_by = 'date'
