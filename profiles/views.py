from django.shortcuts import render, redirect
from .models import *


def profile(request):
    """
    Display the user's profile
    """

    subscriptions = Subscription.objects.all()
    maillist = Maillist.objects.all()

    context = {
        'user': request.user,
        'subscriptions': subscriptions,
        'maillist' : maillist,
    }

    return render(request, 'profiles/profile.html', context)


def maillist_signup(request):
    """
    Render the newsletter signup form
    """
    if request.method == "POST":
        user = request.user
        email = request.POST.get('user_email')

        Maillist.objects.create(user=user, email=email)

        return redirect('profile')

    context = {
        'user': request.user,
    }

    return render(request, 'profiles/newsletter_signup.html', context)
