from django.shortcuts import render, get_object_or_404
from .models import Membership
from django.conf import settings
import os
import stripe
if os.path.exists("env.py"):
    import env

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
    STRIPE_PK = os.environ.get("STRIPE_PK")

    context = {
        'membership': membership,
        'STRIPE_PK': STRIPE_PK,
    }

    return render(request, 'memberships/membership_details.html', context)