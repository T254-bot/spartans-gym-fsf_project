from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_memberships, name='memberships'),
    path('<membership_id>', views.membership_details, name='membership_details'),
]