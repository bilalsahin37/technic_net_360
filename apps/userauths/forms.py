# apps/userauths/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)  # Zorunlu alanları belirtin


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]  # Güncellenebilir alanlar
