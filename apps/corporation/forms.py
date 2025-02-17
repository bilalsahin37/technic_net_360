from django import forms
from django.forms import DateTimeInput
from .models import Customer, ServiceAppointment, Vehicle


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["user", "first_name", "last_name", "email", "phone", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3}),
        }


class ServiceAppointmentForm(forms.ModelForm):
    appointment_date = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}), label="Randevu Tarihi"
    )
    estimated_completion = forms.DateTimeField(
        widget=DateTimeInput(attrs={"type": "datetime-local"}),
        label="Tahmini Tamamlanma",
        required=False,
    )

    class Meta:
        model = ServiceAppointment
        fields = [
            "vehicle",
            "appointment_date",
            "description",
            "workflow_status",
            "technician",
            "estimated_completion",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "owner",
            "brand",
            "model",
            "year",
            "plate_number",
            "vin",
            "color",
            "mileage",
            "fuel_type",
            "transmission",
        ]
        widgets = {
            "year": forms.NumberInput(attrs={"min": 1900}),
            "mileage": forms.NumberInput(attrs={"min": 0}),
        }
