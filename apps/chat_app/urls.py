from django.urls import path, re_path
from .views import Home
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', Home.as_view(), name='home'),



]