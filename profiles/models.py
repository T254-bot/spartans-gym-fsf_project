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
    membership = models.OneToOneField(Membership, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_subscription(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        Subscription.objects.create(user=instance)
    # Existing users: just save the profile
    instance.subscription.save()
