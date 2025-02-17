# apps/technic_service/forms.py
from django import forms

from .models import Customer, ServiceAppointment, Vehicle


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "phone", "address"]
        widgets = {
            "address": forms.Textarea(attrs={"rows": 3, "class": "form-control"})
        }


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            "owner",
            "brand",  # This will now work since VehicleBrand is defined
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
            "brand": forms.Select(attrs={"class": "form-control"}),
        }


class ServiceAppointmentForm(forms.ModelForm):
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



