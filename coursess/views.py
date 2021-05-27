from django import forms
from django.http.response import Http404
from django.shortcuts import render,get_object_or_404
from .models import Course
from  .forms import ContactCourse

#from django.views.generic import DetailView


def index(request):
    courses = Course.objects.all()
    template_name = 'index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)
    

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.method == 'POST':
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()
    context = {
        'course': course,
        'form': form
    }
    template_name = 'details.html'
    return render(request, template_name, context)


