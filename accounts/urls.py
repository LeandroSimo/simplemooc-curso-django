from django.urls import path,include 
from django.conf.urls import url
from django.views.generic import TemplateView



app_name = 'accounts'
urlpatterns = [

    path('entrar/', TemplateView.as_view(template_name="login.html"),name='login'),
    #path('entrar/', include('django.contrib.auth.views.login', {'template_name':'login.html'}, name='login')),
    #path(r'^entrar/$', login, name='login'),

    

]