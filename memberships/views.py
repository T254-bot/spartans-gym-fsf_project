from django.shortcuts import render, get_object_or_404
from .models import Membership
from django.conf import settings
import stripe
stripe.api_key = setting.STRIPE_SECRET_KEY

# Create your views here.

def all_memberships(request):
    """A view display the different membership options"""

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }
    return render(request, 'memberships/memberships.html', context)


def membership_details(request, membership_id):
    membership = get_object_or_404(Membership, pk=membership_id)

    # Retrieve or set up Stripe Customer
    stripe_customer_id = request.user.stripe_customer_id
    if not stripe_customer_id:
        customer = stripe.Customer.create(email=request.user.email)
        stripe_customer_id = customer.id
        request.user.stripe_customer_id = stripe_customer_id
        request.user.save()

    # Create checkout session based on membership type
    if membership.id == 1 or membership.id == 2:  # Subscription memberships
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': membership.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='subscription',  # Use 'subscription' mode for recurring payments
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )
    elif membership.id == 3:  # One-time payment membership
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': membership.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',  # Use 'payment' mode for one-time payment
            success_url=request.build_absolute_uri('/success/'),
            cancel_url=request.build_absolute_uri('/cancel/'),
        )

    context = {
        'membership': membership,
        'checkout_session_id': checkout_session.id,
    }

    return render(request, 'memberships/membership_details.html', context)