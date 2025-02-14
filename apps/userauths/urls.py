# apps/users/urls.py

from django.urls import path
from .views import (
    UserListView,
    UserDetailView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    ProfileDetailView,
    ProfileCreateView,
    ProfileUpdateView,
    ProfileDeleteView,
)

urlpatterns = [
    # Kullanıcı URL'leri
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("users/create/", UserCreateView.as_view(), name="user_create"),
    path("users/<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
    # Profil URL'leri
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profiles/create/", ProfileCreateView.as_view(), name="profile_create"),
    path(
        "profiles/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"
    ),
    path(
        "profiles/<int:pk>/delete/", ProfileDeleteView.as_view(), name="profile_delete"
    ),
]
