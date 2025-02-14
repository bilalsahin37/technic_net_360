# apps/users/views.py

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import (
    User,
    Profile,
    Gender,
    Nationality,
    Job,
    Speciality,
    Duty,
    Address,
    SocialMediaProfile,
    UserPreference,
    EducationLevel,
    EducationField,
    School,
    SchoolDepartment,
    Language,
    Talent,
    Hobby,
)

# Kullanıcı İşlemleri


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"  # Şablon dosyasının yolu
    context_object_name = "users"


class UserDetailView(DetailView):
    model = User
    template_name = "users/user_detail.html"
    context_object_name = "user"


class UserCreateView(CreateView):
    model = User
    fields = [
        "email",
        "phone_number",
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "nationality",
        "identity_number",
        "passport_number",
        "job",
        "speciality",
        "duty",
        "place_of_work",
        "place_of_work_unit",
        "language",
        "hobbies",
        "talents",
        "education_level",
        "education_field",
        "school",
        "school_department",
        "graduation_year",
        "is_verified",
        "is_active",
        "is_superuser",
        "is_admin",
        "is_staff",
        "is_customer",
    ]
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")


class UserUpdateView(UpdateView):
    model = User
    fields = [
        "phone_number",
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "nationality",
        "identity_number",
        "passport_number",
        "job",
        "speciality",
        "duty",
        "place_of_work",
        "place_of_work_unit",
        "language",
        "hobbies",
        "talents",
        "education_level",
        "education_field",
        "school",
        "school_department",
        "graduation_year",
        "is_verified",
        "is_active",
        "is_superuser",
        "is_admin",
        "is_staff",
        "is_customer",
    ]
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user_list")


# Profil İşlemleri


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "users/profile_detail.html"
    context_object_name = "profile"


class ProfileCreateView(CreateView):
    model = Profile
    fields = ["user", "biography", "profile_picture", "website", "location"]
    template_name = "users/profile_form.html"
    success_url = reverse_lazy(
        "user_list"
    )  # Alternatif olarak ayrı bir liste sayfası da kullanılabilir


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ["biography", "profile_picture", "website", "location"]
    template_name = "users/profile_form.html"
    success_url = reverse_lazy("user_list")


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = "users/profile_confirm_delete.html"
    success_url = reverse_lazy("user_list")


# Diğer modeller için de benzer CRUD yapıları uygulanabilir.
