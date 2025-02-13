from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms


# Müşteri Oluşturma Sayfası
class CustomerCreateView(generic.CreateView):
    model = models.Customer
    form_class = forms.CustomerForm
    success_url = reverse_lazy('technic_service:customer_list')
    template_name = 'technic_service/customer_create_form.html'
    fields = '__all__'
    context_object_name = 'customer'




# Müşteri Listesi Sayfası
class CustomerListView(generic.ListView):
    model = models.Customer
    template_name = 'technic_service/customer_list.html'
    context_object_name = 'customers'
    ordering = ['-created_at']
    queryset = models.Customer.objects.all()
    paginate_by = 10







# Müşteri Düzenleme Sayfası
class CustomerUpdateView(generic.UpdateView):
    model = models.Customer
    form_class = forms.CustomerForm
    success_url = reverse_lazy('technic_service:customer_list')
    template_name = 'technic_service/customer_update_form.html'
    fields = '__all__'
    context_object_name = 'customer'
    success_url = reverse_lazy('technic_service:customer_list')
    success_message = 'Müşteri başarıyla güncellendi.'







# Müşteri Silme Sayfası
class CustomerDeleteView(generic.DeleteView):
    model = models.Customer
    success_url = reverse_lazy('technic_service:customer_list')
    success_message = 'Müşteri başarıyla silindi.'
    template_name = 'technic_service/customer_delete_form.html'
    context_object_name = 'customer'







# Müşteri Detay Sayfası
class CustomerDetailView(generic.DetailView):
    model = models.Customer
    template_name = 'technic_service/customer_detail.html'
    context_object_name = 'customer'






# İş Akışı Listesi Sayfası
class WorkFlowListView(generic.ListView):
    model = models.WorkFlow
    template_name = 'technic_service/workflow_list.html'
    context_object_name = 'workflows'
    ordering = ['-created_at']
    queryset = models.WorkFlow.objects.all()
    paginate_by = 10







# İş Akışı Oluşturma Sayfası
class WorkFlowCreateView(generic.CreateView):
    model = models.WorkFlow
    form_class = forms.WorkFlowForm
    success_url = reverse_lazy('technic_service:workflow_list')
    success_message = 'İş akışı başarıyla oluşturuldu.'
    template_name = 'technic_service/workflow_create_form.html'
    fields = '__all__'
    context_object_name = 'workflow'







# İş Akışı Düzenleme Sayfası
class WorkFlowUpdateView(generic.UpdateView):
    model = models.WorkFlow
    form_class = forms.WorkFlowForm
    success_url = reverse_lazy('technic_service:workflow_list')
    success_message = 'İş akışı başarıyla güncellendi.'
    template_name = 'technic_service/workflow_update_form.html'
    fields = '__all__'
    context_object_name = 'workflow'







# İş Akışı Silme Sayfası
class WorkFlowDeleteView(generic.DeleteView):
    model = models.WorkFlow
    success_url = reverse_lazy('technic_service:workflow_list')
    success_message = 'İş akışıasbourgarıyla silindi.'
    template_name = 'technic_service/workflow_delete_form.html'
    context_object_name = 'workflow'








# İş Akışı Detay Sayfası
class WorkFlowDetailView(generic.DetailView):
    model = models.WorkFlow
    template_name = 'technic_service/workflow_detail.html'
    context_object_name = 'workflow'







# Servis Randevusu Listesi
class ServiceAppointmentListView(generic.ListView):
    model = models.ServiceAppointment
    template_name = 'technic_service/serviceappointment_list.html'
    context_object_name = 'serviceappointments'
    ordering = ['-created_at']
    queryset = models.ServiceAppointment.objects.all()
    paginate_by = 10


    




# Servis Randevusu Oluşturma Sayfası
class ServiceAppointmentCreateView(generic.CreateView):
    model = models.ServiceAppointment
    form_class = forms.ServiceAppointmentForm
    success_url = reverse_lazy('technic_service:serviceappointment_list')
    template_name = 'technic_service/serviceappointment_create_form.html'
    fields = '__all__'
    context_object_name = 'serviceappointment'





# Servis Randevusu Düzenleme Sayfası 
class ServiceAppointmentUpdateView(generic.UpdateView):
    model = models.ServiceAppointment
    form_class = forms.ServiceAppointmentForm
    success_url = reverse_lazy('technic_service:serviceappointment_list')
    template_name = 'technic_service/serviceappointment_update_form.html'
    fields = '__all__'
    context_object_name = 'serviceappointment'






# Servis Randevusu Silme Sayfası
class ServiceAppointmentDeleteView(generic.DeleteView):
    model = models.ServiceAppointment
    success_url = reverse_lazy('technic_service:serviceappointment_list')
    template_name = 'technic_service/serviceappointment_delete_form.html'
    context_object_name = 'serviceappointment'
    success_message = 'Servis randevusu başarıyla silindi.'







# Servis Randevusu Detay Sayfası
class ServiceAppointmentDetailView(generic.DetailView):
    model = models.ServiceAppointment
    template_name = 'technic_service/serviceappointment_detail.html'
    context_object_name = 'serviceappointment'