
from django.contrib import admin 
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path





urlpatterns = [
       
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('cursos/', include('coursess.urls', namespace='courses')),
    path('conta/', include('accounts.urls', namespace='accounts')),
    
    
   

    #LOGIN, LOGOUT, PASSWORD:     
    path('', include('django.contrib.auth.urls')),
     




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
#    urlpatterns += static(
#        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
