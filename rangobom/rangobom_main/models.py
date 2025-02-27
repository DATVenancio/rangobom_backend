from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
