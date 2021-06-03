from django import forms
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Enrollment
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
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()
            
    else:
        form = ContactCourse()
    context['form'] = form
    context['course'] = course
    template_name = 'details.html'
    return render(request, template_name, context)

@login_required
def enrollment(request,slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    if created:
        #enrollment.active()
        messages.success(request, 'Você foi inscrito no curso com sucesso')
    else:
        messages.info(request, 'Você já está inscrito no curso')


    return redirect('accounts:dashboard')
