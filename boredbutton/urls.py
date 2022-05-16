from os import stat
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('' , include ('boredbuttonapp.urls')),
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('/media/boredbuttonfav.png')))
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
