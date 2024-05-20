from django.shortcuts import render
from .models import Subscription


def profile(request):
    """
    Display the user's profile
    """

    subscriptions = Subscription.objects.all()

    context = {
        'user': request.user,
        'subscriptions': subscriptions,
    }

    return render(request, 'profiles/profile.html', context)
