"""
URL configuration for core project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.userauths.views import UserCreateView

from . import views

app_name = "location"

urlpatterns = [
    # Yönetim Paneli
    path("admin/", admin.site.urls),
    # User Authentication: Kullanıcı kayıt, giriş vb.
    path("accounts/", include("apps.userauths.urls", namespace="userauths")),
    path("signup/", UserCreateView.as_view()),
    # Corporation: Kurum bilgileri ve işlemleri
    path("corporations/", include("apps.corporation.urls")),
    # Technic Service: Teknik servis işlemleri
    path("technic-service/", include("apps.technic_service.urls")),
    # Add your URL patterns here
]

# DEBUG modunda statik ve medya dosyaları için URL yapılandırması
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
