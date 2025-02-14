from django.urls import path
from .views import (
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserListView,
    UserDetailView,
)

app_name = "userauths"  # Uygulama isim alanı (namespace)

urlpatterns = [
    # Kullanıcı Kayıt Sayfası
    path("signup/", UserCreateView.as_view(), name="user-create"),
    # Kullanıcı Güncelleme Sayfası (pk: primary key parametresi)
    path("update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    # Kullanıcı Silme Sayfası
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
    # Kullanıcı Listeleme Sayfası
    path("list/", UserListView.as_view(), name="user-list"),
    # Kullanıcı Detay Sayfası
    path("detail/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
]
