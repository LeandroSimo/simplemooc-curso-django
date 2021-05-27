from django.urls import path
from .views import index, details


app_name = 'courses'
urlpatterns = [

    path('', index, name='index'),
    path('(?p<slug>[\w-]*)', details, name='details'),

   

]