"""
URL configuration for core project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.userauths.views import UserCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("apps.userauths.urls")),
    path("corporation/", include("apps.corporation.urls")),
    path("technic-service/", include("apps.technic_service.urls")),
]

# URL configuration for static and media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
