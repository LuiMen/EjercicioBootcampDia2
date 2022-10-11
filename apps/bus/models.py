from django.db import models

from apps.brand.models import Brand
from apps.location.models import Location


class Bus(models.Model):
    number = models.PositiveSmallIntegerField(verbose_name='Número')
    plate = models.CharField(max_length=10)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    origin = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,
                               related_name='origin')
    destiny = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,
                                related_name='destiny')

    class Meta:
        verbose_name = 'Autobús'
        verbose_name_plural = 'Autobuses'

    def __str__(self):
        return '%s (%s)' % (self.number, self.plate)
