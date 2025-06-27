from django.db import models
from django.contrib.auth.models import User
from account.models import Profile

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Jméno") 
    cost = models.PositiveIntegerField(verbose_name="Cena")
    profit = models.PositiveIntegerField(verbose_name="Vydělává")
    type = "product"

    def __str__(self):
        return f"Budova: {self.name}" 

class Upgrade(models.Model):
    name = models.CharField(max_length=100, verbose_name="Jméno") 
    cost = models.PositiveIntegerField(verbose_name="Cena")
    description = models.CharField(max_length=1000, verbose_name="Popis")
    type = "upgrade"

    def __str__(self):
        return f"Vylepšení: {self.name}" 