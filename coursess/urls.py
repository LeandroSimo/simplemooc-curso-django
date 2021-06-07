from django.urls import path, re_path
from django.urls.conf import include

from . import views

app_name = 'courses'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<slug>[\w_-]+)/$',views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/inscrição/$',views.enrollment, name='enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/cancelar-inscrição/$',views.undo_enrollment, name='undo_enrollment'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/$',views.announcements, name='announcements'),
    re_path(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$',views.show_announcements, name='show_announcement'),
    re_path(r'^(?P<slug>[\w_-]+)/aulas/$',views.lessons, name='lessons'),
    re_path(r'^(?P<slug>[\w_-]+)/aula/(?P<pk>\d+)/$',views.lesson, name='lesson'),
    re_path(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$',views.material, name='material'),
    #path('<slug:slug>/', CourseDetailSlugView.as_view()),
    #url('^(?P<slug>[\w_-]+)$', details, name='details'),
    #path('^(?P<slug>[\w_-]+)/$', details, name='details'),

   

]