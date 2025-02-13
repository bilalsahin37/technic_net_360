from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import forms


class UserCreateView(generic.CreateView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
