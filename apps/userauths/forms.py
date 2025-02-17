# apps/userauths/forms.py
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)  # Specify required fields


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]  # Updatable fields

# apps/technic_service/forms.py
from django import forms
from .models import Customer, Vehicle, ServiceAppointment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

# apps/technic_service/views.py
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from . import forms

class CustomerCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = forms.CustomerForm
    template_name = "technic_service/customer_form.html"
    success_message = "Müşteri başarıyla oluşturuldu."
