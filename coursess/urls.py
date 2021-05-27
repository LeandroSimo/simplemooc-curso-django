from django.urls import path
from .views import index


app_name = 'courses'
urlpatterns = [

    path('', index, name='index'),
   

]