from datetime import timezone
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.utils import timezone
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import OneToOneField, ForeignKey

# Create your models here.
class Greenhouse(models.Model):
    greenhouse = models.CharField(max_length=220)

    def __str__(self) -> str:
        return self.greenhouse

class Planter(models.Model):
    greenhouse = ForeignKey(Greenhouse, on_delete=CASCADE)
    plants = CharField(max_length=220)

    def __str__(self) -> str:
        return f'{self.plants}'

class Soilmoisture(models.Model):
    greenhouse = ForeignKey(Greenhouse, on_delete=CASCADE)
    planter = ForeignKey(Planter, on_delete=CASCADE)
    date = models.DateTimeField(default=timezone.now)
    value = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.date} {self.greenhouse}: {self.planter} soil moisture: {self.value}'

class Humidity(models.Model):
    greenhouse = ForeignKey(Greenhouse, on_delete=CASCADE)
    date = models.DateTimeField(default=timezone.now)
    value = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.date} {self.greenhouse} Moisture: {self.value}'

class Temperature(models.Model):
    greenhouse = ForeignKey(Greenhouse, on_delete=CASCADE)
    date = models.DateTimeField(default=timezone.now)
    value = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.date} {self.greenhouse} Temperature: {self.value}'


