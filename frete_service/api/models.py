from django.db import models

# Create your models here.
class Frete(models.Model):
    produto = models.CharField(max_length=100)