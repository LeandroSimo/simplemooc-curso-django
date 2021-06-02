from django.urls import path, re_path
from django.urls.conf import include

from . import views

app_name = 'courses'
urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<slug>[\w_-]+)/$',views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/inscrição/$',views.enrollment, name='enrollment'),
    #path('<slug:slug>/', CourseDetailSlugView.as_view()),
    #url('^(?P<slug>[\w_-]+)$', details, name='details'),
    #path('^(?P<slug>[\w_-]+)/$', details, name='details'),

   

]