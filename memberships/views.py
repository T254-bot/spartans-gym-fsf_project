from django.shortcuts import render
from .models import Membership

# Create your views here.

def all_memberships(request):
    """A view display the different membership options"""

    memberships = Membership.objects.all()

    context = {
        'memberships': memberships,
    }
    return render(request, 'memberships/memberships.html', context)
