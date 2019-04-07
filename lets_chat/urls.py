"""lets_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from chat_app.views import Signup, logout
from apps import chat_app
from django.contrib.auth.views import PasswordChangeView

urlpatterns = [
    path('', include('chat_app.urls')),
    path('admin/', admin.site.urls),
    # re_path(r'^accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout_login/', logout, name='logout_login'),
    # path('accounts/password_change/', PasswordChangeView.as_view(template_name='password_change_form.html'),name='password_change'),
]
