from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout_then_login
from django.views.generic.list import ListView
from django.views.generic import TemplateView
import json
from django.urls import  reverse


class Home(View):

    def post(self, request, *args, **kwargs):
        print(request.POST, ' .....  request.data')
        print(request.body, ' .....  request.body')
        print(kwargs, ' .....  kwargs')
        print(args, ' .....  args')
        return render(request, 'home.html')


class Signup(View):

    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')


def logout(request):
    return logout_then_login(request)
