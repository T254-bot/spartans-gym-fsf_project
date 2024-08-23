from django.shortcuts import render, redirect
from django.contrib import messages
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


def maillist_update(request):
    """
    Render the newsletter update form
    """
    if request.method == 'POST':
        new_email = request.POST.get('user_email')
        if new_email:
            request.user.email = new_email
            request.user.save()
            messages.success(request, 'Your email has been updated!')
        return redirect('profile')

    return render(request, 'profiles/newsletter_update.html')

def maillist_delete(request):
    """
    Delete users email from mail list
    """
    user = request.user
    maillist = Maillist.objects.all()


    return render(request, 'profiles/newsletter_update.html')