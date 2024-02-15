from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.sitio.urls')),
]

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),
]
