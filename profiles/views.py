from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *


def profile(request):
    """
    Display the user's profile
    """

    subscriptions = Subscription.objects.filter(user=request.user.email)
    maillist = Maillist.objects.filter(user=request.user)

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
            # Assuming `MailList` has a foreign key to `User` as `user`
            maillist_entry = get_object_or_404(Maillist, user=request.user)
            maillist_entry.email = new_email
            maillist_entry.save()
            messages.success(request, 'Your email has been updated!')
        return redirect('profile')

    return render(request, 'profiles/newsletter_update.html')

def maillist_delete(request):
    """
    Delete users email from mail list
    """
    if request.method == 'POST':
        maillist_entry = get_object_or_404(Maillist, user=request.user)

        maillist_entry.delete()

        messages.success(request, 'Your email has been removed from the Mail list')
        return redirect('profile')
    return redirect('profile')