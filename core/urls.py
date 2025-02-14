"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.userauths.views import  UserCreateView


urlpatterns = [
    # Yönetim Paneli
    path("admin/", admin.site.urls),
    # User Authentication: Kullanıcı kayıt, giriş vb.
    path("accounts/", include("apps.userauths.urls", namespace="userauths")),
    # Corporation: Kurum bilgileri ve işlemleri
    path("corporations/", include("apps.corporation.urls", namespace="corporation")),
    # Technic Service: Teknik servis işlemleri
    path(
        "technic-service/",
        include("apps.technic_service.urls", namespace="technic_service"),
    ),
    # Location: Konum ve yer bilgileri yönetimi
    path("locations/", include("apps.location.urls", namespace="location")),
]

# DEBUG modunda statik ve medya dosyaları için URL yapılandırması
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
