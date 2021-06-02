
from django.contrib import admin 
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import re_path


urlpatterns = [
    re_path(r'^', include('core.urls', namespace='core')),
    path('admin/', admin.site.urls),
    path('conta/', include('accounts.urls', namespace='accounts')),
    path('cursos/', include('coursess.urls', namespace='courses')),
    #LOGIN, LOGOUT, PASSWORD:     

] 

if settings.DEBUG:  # Use local only
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)  # For serving media files
