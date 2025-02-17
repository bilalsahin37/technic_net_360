"""
URL configuration for core project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.userauths.views import UserCreateView

urlpatterns = [
    # Admin Panel
    path("admin/", admin.site.urls),
    # User Authentication: User registration, login, etc.
    path("accounts/", include("apps.userauths.urls")),
    path("signup/", UserCreateView.as_view()),
    # Corporation: Corporation information and operations
    path("corporations/", include("apps.corporation.urls")),
    # Technic Service: Technical service operations
    path("technic-service/", include("apps.technic_service.urls")),
    # Add your URL patterns here
]

# URL configuration for static and media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
