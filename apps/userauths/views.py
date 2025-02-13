from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from . import models
from . import forms

# Model referansını doğru şekilde al
User = get_user_model()


# Kullanıcı Kayıt Sayfası
class UserCreateView(generic.CreateView):
    model = User
    template_name = "registration/user_form.html"
    form_class = forms.UserCreationForm  # Özel form kullanımı
    success_url = reverse_lazy("login")
    success_message = "Kayıt oluşturuldu."


# Kullanıcı Güncelleme Sayfası
class UserUpdateView(generic.UpdateView):
    model = User
    template_name = "registration/user_form.html"
    form_class = forms.UserUpdateForm  # forms.py'de tanımlanmalı
    success_url = reverse_lazy("home")


# Kullanıcı Silme Sayfası
class UserDeleteView(generic.DeleteView):
    model = User
    template_name = "registration/user_confirm_delete.html"
    success_url = reverse_lazy("home")


# Kullanıcı Listeleme Sayfası
class UserListView(generic.ListView):
    model = User
    template_name = "registration/user_list.html"
    context_object_name = "users"
    ordering = ["-date_joined"]
    paginate_by = 10


class UserDetailView(generic.DetailView):
    model = User
    template_name = "registration/user_detail.html"
    context_object_name = "user"
