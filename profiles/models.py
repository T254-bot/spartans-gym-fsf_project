from django.db import models
from memberships.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Subscription(models.Model):
    """
    Create a subscription object 
    """
    user = models.EmailField(max_length=254)
    membership = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.user.username

class Maillist(models.Model):
    """
    Create a mail list object
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)