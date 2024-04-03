from django.db import models

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    cost = models.CharField(max_length=50, default=1)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='path/to/my/default/image.jpg')
    description = models.CharField(max_length=254)