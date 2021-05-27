from django.urls import path
from .views import home
from .views import contact 


# namespace: app_name = 'core'
urlpatterns = [

    path('', home, name='home'),
    path('contato/', contact, name='contact'),

]