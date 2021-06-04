from django import forms
from django.db.models.query import ValuesIterable
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.defaultfilters import escapejs_filter
from .models import Course, Enrollment, Announcement
from  .forms import ContactCourse, CommentForm


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


@login_required
def undo_enrollment(request, slug):
    course = get_object_or_404(Course, slug=slug)
    enrollment = get_object_or_404(
            Enrollment, user=request.user, course=course
        )
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Sua inscrição foi cancelada com sucesso')
        return redirect('accounts:dashboard')
    template_name = 'undo_enrollment.html'
    context = {
        'enrollment': enrollment,
        'course': course
    }
    return render(request, template_name, context)

@login_required
def announcements(request,slug):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollment, user=request.user, course=course
        )
        if not enrollment.is_approved():
            messages.error(request, 'Inscrição pendente')
        return redirect('accounts:dashboard')
    template_name = 'announcements.html'
    context = {
        'course': course,
        'announcements': course.announcements.all()
    }
    return render(request, template_name, context )

@login_required
def show_announcements(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    if not request.user.is_staff:
        enrollment = get_object_or_404(
            Enrollment, user=request.user, course=course
        )
        if not enrollment.is_approved():
            messages.error(request, 'Inscrição pendente')
        return redirect('accounts:dashboard')
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.announcement = announcement
        comment.save()
        form = CommentForm()
        messages.success(request, 'Comentário salvo!')
    template_name = 'show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form     
    }
    return render(request, template_name, context)
