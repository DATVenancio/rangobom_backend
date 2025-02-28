from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    profile_image_url= models.CharField(max_length=200,null=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
