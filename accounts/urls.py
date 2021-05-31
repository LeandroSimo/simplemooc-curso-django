from django.urls.conf import re_path
from accounts.views import register
from django.urls import path,include 
from django.conf.urls import url
from django.views.generic import TemplateView



app_name = 'accounts'
urlpatterns = [
    path('', TemplateView.as_view(template_name="dashboard.html"),name='dashboard'),

    path('entrar/', TemplateView.as_view(template_name="login.html"),name='login'),
    path('cadastre-se/', register,name='register'),
    re_path('sair/', TemplateView.as_view(template_name="home.html"), name='logout'),
   
    
    #path('entrar/', include('django.contrib.auth.views.login', {'template_name':'login.html'}, name='login')),
    #path(r'^entrar/$', login, name='login'),

    

]