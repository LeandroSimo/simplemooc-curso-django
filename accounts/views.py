from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .forms import ResgisterForm


def register(request):
    template_name = 'register.html'
    if request.method == "POST":
        form = ResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
         form = ResgisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)




