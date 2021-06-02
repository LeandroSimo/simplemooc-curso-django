from django.conf.urls import url
from django.urls.conf import include, path, re_path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import views as auth

#from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
    re_path(r'^entrar/$', auth.LoginView.as_view(template_name='registration/login.html'), name='login'), 
    re_path(r'^sair/$', auth.LogoutView.as_view(), name='logout'),
    re_path(r'^$',views.dashboard, name='dashboard'),
    re_path(r'^cadastre-se/$',views.register, name='register'),
    re_path(r'^nova-senha/$',views.password_reset, name='password_reset'),
    re_path(r'^editar/$',views.edit, name='edit'),
    re_path(r'^editar-senha/$',views.edit_password, name='edit_password'),
        

    #re_path(r'^sair/$',views.logout_view, name='logout'),
    #path('cadastre-se', TemplateView.as_view(template_name="register.html"),name='register'),
    #path(r'^cadastre-se/$', 'curso.accounts.views.register', name='register'),
    #path('cadastre-se', include('django.contrib.auth.urls.register')),
   
   

]