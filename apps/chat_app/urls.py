from django.urls import path, include, re_path
from .views import Home
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from.api import api_urls

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/<int:id>/<str:name>/', Home.as_view(), name='home'),
    path('users/', TemplateView.as_view(template_name='users.html'), name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('chat_app.api.api_urls')),
]
