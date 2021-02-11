import datetime
from enum import Enum

from django.db import models


class Make(models.TextChoices):
    Ford = 'FORD', 'Ford'
    Holden = 'HOLDEN', 'Holden'
    Mazda = 'MAZDA', 'Mazda'
    Toyota = 'TOYOTA', 'Toyota'
    Nissan = 'NISSAN', 'Nissan'


class Model(models.TextChoices):
    Falcon = 'Falcon'
    Epica = 'Epica'
    Camry = 'Camry'
    CX5 = 'CX-5'


Years = sorted([(y, str(y)) for y in range(1970, datetime.datetime.now().year)], reverse=True)


class Condition(models.TextChoices):
    Poor = 'Poor'
    Fair = 'Fair'
    Good = 'Good'
    Excellent = 'Excellent'


class Car(models.Model):
    SellerName = models.CharField(max_length=100)
    SellerMobile = models.CharField(max_length=15)
    Make = models.CharField(max_length=20, choices=Make.choices)
    Model = models.CharField(max_length=100, choices=Model.choices)
    Year = models.IntegerField(choices=Years, default=Years[2])
    Condition = models.CharField(max_length=10, choices=Condition.choices, default=Condition.Fair)
    AskingPrice = models.IntegerField(default=1000)


    def __str__(self):
        return f'{self.Make} {self.Model}: {self.Year}, {self.Condition}'

    class Meta:
        ordering = ["id",]