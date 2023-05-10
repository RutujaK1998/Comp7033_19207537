from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
