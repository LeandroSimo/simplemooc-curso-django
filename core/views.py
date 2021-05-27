from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render (request, 'home.html',)

def contact(request):
    return render(request, 'contact.html')
