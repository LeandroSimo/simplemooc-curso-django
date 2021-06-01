from accounts.views import register
from django.conf.urls import url
from django.urls.conf import include, path, re_path
from django.views.generic import TemplateView

from . import views

#from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [

    re_path('',views.dashboard, name='dashboard'),
    re_path(r'^cadastre-se/$',views.register, name='register'),
    
    
    #re_path(r'^sair/$',views.logout_view, name='logout'),
    #path('cadastre-se', TemplateView.as_view(template_name="register.html"),name='register'),
    #path(r'^cadastre-se/$', 'curso.accounts.views.register', name='register'),
    #path('cadastre-se', include('django.contrib.auth.urls.register')),
   
   

]