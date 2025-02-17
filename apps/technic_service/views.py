# views.py
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic

from .forms import CustomerForm, ServiceAppointmentForm, VehicleForm  # Direct imports
from .models import Customer, ServiceAppointment, Vehicle


class CustomerLitsView(SuccessMessageMixin, generic.ListView):
    model = Customer
    template_name = "technic_service/customer_list.html"
    context_object_name = "customers"
    success_message = "Müşteriler başarıyla listelendi."


class CustomerUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "technic_service/customer_form.html"
    success_message = "Customer successfully updated."
    success_message = "Müşteri başarıyla güncellendi."
    model = Customer
    template_name = "technic_service/customer_list.html"
    context_object_name = "customers"


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = "technic_service/customer_detail.html"
    context_object_name = "customer"


class VehicleCreateView(SuccessMessageMixin, generic.CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "technic_service/vehicle_form.html"
    success_message = "Vehicle successfully created."
    success_message = "Araç başarıyla oluşturuldu."

    success_message = "Araç başarıyla oluşturuldu."
    model = Vehicle
    template_name = "technic_service/vehicle_detail.html"
    context_object_name = "vehicle"


class ServiceAppointmentCreateView(SuccessMessageMixin, generic.CreateView):
    model = ServiceAppointment
    form_class = ServiceAppointmentForm
    template_name = "technic_service/appointment_form.html"
    success_message = "Service appointment successfully created."
    success_message = "Servis randevusu başarıyla oluşturuldu."


class ServiceAppointmentUpdateView(SuccessMessageMixin, generic.UpdateView):
    success_message = "Servis randevusu başarıyla oluşturuldu."
    template_name = "technic_service/appointment_form.html"
    success_message = "Service appointment successfully updated."
    success_message = "Servis randevusu başarıyla güncellendi."


class ServiceAppointmentListView(generic.ListView):
    model = ServiceAppointment
    success_message = "Servis randevusu başarıyla güncellendi."

    success_message = "Servis randevusu başarıyla oluşturuldu."
    template_name = "technic_service/appointment_detail.html"
    context_object_name = "appointment"
    template_name = "technic_service/appointment_form.html"
    success_message = "Servis randevusu başarıyla güncellendi."
