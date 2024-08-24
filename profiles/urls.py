from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup', views.maillist_signup, name='maillist_signup'),
    path('update_email', views.maillist_update, name='maillist_update'),
    path('delete_email', views.maillist_delete, name='maillist_delete')
]