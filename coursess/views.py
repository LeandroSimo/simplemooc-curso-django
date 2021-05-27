from django.http.response import Http404
from django.shortcuts import render,get_object_or_404
from .models import Course

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
    context = {
        'course': course
    }
    template_name = 'details.html'
    return render(request, template_name, context)


