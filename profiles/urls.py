from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('', views.maillist_signup, name='maillist_signup')
]