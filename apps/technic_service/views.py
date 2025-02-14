# views.py
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from . import forms
from .models import Customer, Vehicle, ServiceAppointment, ServiceRecord


class CustomerCreateView(SuccessMessageMixin, generic.CreateView):
    model = Customer
    form_class = forms.CustomerForm
    template_name = "technic_service/customer_form.html"
    success_url = reverse_lazy("customer-list")
    success_message = "Müşteri başarıyla oluşturuldu."


class CustomerUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Customer
    form_class = forms.CustomerForm
    template_name = "technic_service/customer_form.html"
    success_url = reverse_lazy("customer-list")
    success_message = "Müşteri başarıyla güncellendi."


class CustomerListView(generic.ListView):
    model = Customer
    template_name = "technic_service/customer_list.html"
    context_object_name = "customers"


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = "technic_service/customer_detail.html"
    context_object_name = "customer"


class VehicleCreateView(SuccessMessageMixin, generic.CreateView):
    model = Vehicle
    form_class = forms.VehicleForm
    template_name = "technic_service/vehicle_form.html"
    success_url = reverse_lazy("vehicle-list")
    success_message = "Araç başarıyla oluşturuldu."


class VehicleUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Vehicle
    form_class = forms.VehicleForm
    template_name = "technic_service/vehicle_form.html"
    success_url = reverse_lazy("vehicle-list")
    success_message = "Araç başarıyla güncellendi."


class VehicleListView(generic.ListView):
    model = Vehicle
    template_name = "technic_service/vehicle_list.html"
    context_object_name = "vehicles"


class VehicleDetailView(generic.DetailView):
    model = Vehicle
    template_name = "technic_service/vehicle_detail.html"
    context_object_name = "vehicle"


class ServiceAppointmentCreateView(SuccessMessageMixin, generic.CreateView):
    model = ServiceAppointment
    form_class = forms.ServiceAppointmentForm
    template_name = "technic_service/appointment_form.html"
    success_url = reverse_lazy("appointment-list")
    success_message = "Servis randevusu başarıyla oluşturuldu."


class ServiceAppointmentUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = ServiceAppointment
    form_class = forms.ServiceAppointmentForm
    template_name = "technic_service/appointment_form.html"
    success_url = reverse_lazy("appointment-list")
    success_message = "Servis randevusu başarıyla güncellendi."


class ServiceAppointmentListView(generic.ListView):
    model = ServiceAppointment
    template_name = "technic_service/appointment_list.html"
    context_object_name = "appointments"


class ServiceAppointmentDetailView(generic.DetailView):
    model = ServiceAppointment
    template_name = "technic_service/appointment_detail.html"
    context_object_name = "appointment"
