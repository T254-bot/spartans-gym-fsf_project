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

    context = {
        'membership': membership,
    }

    return render(request, 'memberships/membership_details.html', context)