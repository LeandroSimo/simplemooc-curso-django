from django.contrib.auth import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

#from django.contrib.auth import logout

from .forms import RegisterForm, EditAccountForm

@login_required
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)



def register(request):
    template_name = 'register.html'
    print("sgsgsgsd")
    try:
        logout(request)
    except:
        pass
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data['password1'])
        login(request, user)
        return redirect('core:home')
    context = {
      'form': form
    }
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
           
    else:
        form = EditAccountForm(instance=request.user)
    context = {'form': form}
    return render(request, template_name, context)



#def logout_view(request):
#    template_name = 'home.html'
#    logout(request)
#   return render ( request, template_name )