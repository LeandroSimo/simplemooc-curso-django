from django.contrib.auth import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login
#from django.contrib.auth import logout

from .forms import RegisterForm

def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('core:home')
    else:
        form = RegisterForm()  
    context = {
      'form': form
    }
    return render(request, template_name, context)

#def logout_view(request):
#    template_name = 'home.html'
#    logout(request)
#   return render ( request, template_name )