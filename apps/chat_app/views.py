from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import logout_then_login

# @login_required


class Home(View):

    def get(self, request, *args, **kargs):
        return render(request, 'home.html')


class Signup(View):

    def get(self, request, *args, **kargs):
        form = UserCreationForm()
        return render(request,'registration/signup.html',{'form':form})

    def post(self, request, *args, **kargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')


def logout(request):
    return logout_then_login(request)
