from django.db import models

# Create your models here.

class Membership(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    length = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1,)
    stripe_price = models.IntegerField(default=1,) 
    stripe_price_id = models.CharField(max_length=255, default='', blank=True)
    image = models.URLField(max_length=200, default='') 

    def __str__(self):
        return self.name