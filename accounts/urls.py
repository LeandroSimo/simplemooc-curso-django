
from accounts.views import login
from django.urls import path,include 
from django.conf.urls import url
from django.views.generic import TemplateView


app_name = 'accounts'
urlpatterns = [

    #path(r'^entrar/$', include('django.contrib.auth.views.urls'), name='login'),
    path('entrar/', TemplateView.as_view(template_name="accounts/login.html"),name='login'),
    #path(r'^entrar/$', login, name='login'),

    

]