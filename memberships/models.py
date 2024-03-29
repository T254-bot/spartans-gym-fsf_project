from django.db import models

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    cost = models.CharField
    image = models.ImageField