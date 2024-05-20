from django.shortcuts import render
import os
import json
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from memberships.models import Membership
if os.path.exists("env.py"):
    import env


stripe.api_key = os.environ.get("STRIPE_SK")


@csrf_exempt
def my_webhook_view(request):
  payload = request.body

  # Retrieve the webhook signature
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']

  # Verify the signature
  try:
      event = stripe.Webhook.construct_event(
          payload, sig_header, 'whsec_e81c157facb226ac295c338d1bb7266764687b7116613562049ebdc2d1e74eef'  #settings.STRIPE_WEBHOOK_SECRET
      )
  except ValueError as e:
      # Invalid payload
      return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
      # Invalid signature
      return HttpResponse(status=400)

  # Handle the event
  if event.type == 'payment_intent.succeeded':

    # Extract relevant information from the event
    amount = event['data']['object']['amount']
    receipt_email = event['data']['object']['receipt_email']

    print('PaymentIntent was successful!')    
    user = User.objects.get(email=receipt_email)
    print(user)
    product = Membership.objects.get(stripe_price=amount)
    print(product)

    messages.add_message(request, messages.INFO, "Hello world.")
  elif event.type == 'payment_method.attached':
    payment_method = event.data.object # contains a stripe.PaymentMethod
    print('PaymentMethod was attached to a Customer!')
  # ... handle other event types
  else:
    print('Unhandled event type {}'.format(event.type))

  product = Membership.objects.get(price=2000)
  user = User.objects.get(email=tyler)
  #subscription.objects.filter(user=request.session.user)

  return HttpResponse(status=200)
