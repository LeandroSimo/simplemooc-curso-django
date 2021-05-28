from django.urls import path, re_path
from django.urls.conf import include
from .views import index, details


app_name = 'courses'
urlpatterns = [

    path('', index, name='index'),
    re_path(r'^(?P<slug>[\w_-]+)/$',details, name='details'),
    #path('<slug:slug>/', CourseDetailSlugView.as_view()),
    #url('^(?P<slug>[\w_-]+)$', details, name='details'),
    #path('^(?P<slug>[\w_-]+)/$', details, name='details'),

   

]