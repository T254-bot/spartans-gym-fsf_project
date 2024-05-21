from django.db import models
from memberships.models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Subscription(models.Model):
    """
    Create a subscription object 
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.OneToOneField(Membership, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
