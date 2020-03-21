from django.urls import path, include
from .api import ListUsers
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('list-users/', ListUsers.as_view(), name='list-users')
]
