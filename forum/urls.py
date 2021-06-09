from courses import urls
from django.urls import path,re_path
from . import views
from django.views.generic import TemplateView

import forum



app_name = 'forum'
urlpatterns = [
     re_path(r'^$', views.index, name='index'),
     re_path(r'^tag/(?P<tag>[\w_-]+)/$', views.index, name='index_tagged'),
     #re_path(r'^$',TemplateView.as_view(template_name="forum/index.html"),name='index'),
     #re_path(r'^tag/(?P<tag>[\w_-]+)/$',TemplateView.as_view(template_name="forum/index.html"),name='index_tagged'),
     re_path(r'^respostas/(?P<pk>\d+)/correta/$',views.reply_correct,name='reply_correct'),
     re_path(r'^respostas/(?P<pk>\d+)/incorreta/$',views.reply_incorrect,name='reply_incorrect'),
     re_path(r'^(?P<slug>[\w_-]+)/$', views.thread,name='thread'),
     #re_path(r'^(?P<slug>[\w_-]+)/$',TemplateView.as_view(template_name="forum/thread.html"),name='thread'),

     #path(r'^$',index,name='index'),
     #re_path(r'^tag/(?P<tag>[\w_-]+)/$',views.index, name='index_tagged'),
]