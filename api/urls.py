from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_webhook_view, name='nothing'),
    path('stripe', views.my_webhook_view, name='webhook'),
]