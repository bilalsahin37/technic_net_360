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





# Servis Kaydı Listesi Sayfası
class ServiceRecordListView(generic.ListView):
    model = models.ServiceRecord
    template_name = 'technic_service/servicerecord_list.html'
    context_object_name = 'servicerecords'
    ordering = ['-created_at']
    queryset = models.ServiceRecord.objects.all()
    paginate_by = 10





# Servis Kaydı Oluşturma Sayfası
class ServiceRecordCreateView(generic.CreateView):
    model = models.ServiceRecord
    form_class = forms.ServiceRecordForm
    success_url = reverse_lazy('technic_service:servicerecord_list')
    success_message = 'Servis kaydınız başarıyla oluşturuldu.'
    template_name = 'technic_service/servicerecord_create_form.html'
    fields = '__all__'
    context_object_name = 'servicerecord'







# Servis Kaydı Düzenleme Sayfası
class ServiceRecordUpdateView(generic.UpdateView):
    model = models.ServiceRecord    
    form_class = forms.ServiceRecordForm
    success_url = reverse_lazy('technic_service:servicerecord_list')
    success_message = 'Servis kaydınız başarıyla güncellendi.'
    template_name = 'technic_service/servicerecord_update_form.html'
    fields = '__all__'
    context_object_name = 'servicerecord'







# Servis Kaydı Silme Sayfası
class ServiceRecordDeleteView(generic.DeleteView):
    model = models.ServiceRecord
    success_url = reverse_lazy('technic_service:servicerecord_list')
    success_message = 'Servis kaydınız başarıyla silindi.'
    template_name = 'technic_service/servicerecord_delete_form.html'
    context_object_name = 'servicerecord'
    







# Servis Kaydı Detay Sayfası
class ServiceRecordDetailView(generic.DetailView):
    model = models.ServiceRecord
    template_name = 'technic_service/servicerecord_detail.html'
    context_object_name = 'servicerecord'







# Servis Detayları Listesi
class ServiceDetailListView(generic.ListView):
    model = models.ServiceDetail
    template_name = 'technic_service/servicedetail_list.html'
    context_object_name = 'servicedetails'
    ordering = ['-created_at']
    queryset = models.ServiceDetail.objects.all()
    paginate_by = 10






# Servis Detayları Oluşturma Sayfası
class ServiceDetailCreateView(generic.CreateView):
    model = models.ServiceDetail
    form_class = forms.ServiceDetailForm
    success_url = reverse_lazy('technic_service:servicedetail_list')
    success_message = 'Servis detaylarınız başarıyla oluşturuldu.'
    template_name = 'technic_service/servicedetail_create_form.html'
    fields = '__all__'
    context_object_name = 'servicedetail'







# Servis Detayları Düzenleme Sayfası
class ServiceDetailUpdateView(generic.UpdateView):
    model = models.ServiceDetail
    form_class = forms.ServiceDetailForm
    success_url = reverse_lazy('technic_service:servicedetail_list')
    success_message = 'Servis detaylarınız başarıyla güncellendi.'
    template_name = 'technic_service/servicedetail_update_form.html'
    fields = '__all__'
    context_object_name = 'servicedetail'







# Servis Detayları Silme Sayfası
class ServiceDetailDeleteView(generic.DeleteView):
    model = models.ServiceDetail
    success_url = reverse_lazy('technic_service:servicedetail_list')
    success_message = 'Servis detaylarınız başarıyla silindi.'
    template_name = 'technic_service/servicedetail_delete_form.html'
    context_object_name = 'servicedetail'






# Arac Listesi
class VehicleListView(generic.ListView):
    model = models.Vehicle
    template_name = 'technic_service/vehicle_list.html'
    context_object_name = 'vehicles'
    ordering = ['-created_at']
    queryset = models.Vehicle.objects.all()
    paginate_by = 10







# Arac Oluşturma Sayfası
class VehicleCreateView(generic.CreateView):
    model = models.Vehicle
    form_class = forms.VehicleForm
    success_url = reverse_lazy('technic_service:vehicle_list')
    success_message = 'Aracınız basarıyla olusturuldu.'
    template_name = 'technic_service/vehicle_create_form.html'
    fields = '__all__'
    context_object_name = 'vehicle'








# Arac Düzenleme Sayfası
class VehicleUpdateView(generic.UpdateView):
    model = models.Vehicle
    form_class = forms.VehicleForm
    success_url = reverse_lazy('technic_service:vehicle_list')
    success_message = 'Aracınız basarıyla güncellendi.'
    template_name = 'technic_service/vehicle_update_form.html'
    fields = '__all__'
    context_object_name = 'vehicle'








# Arac Silme Sayfası
class VehicleDeleteView(generic.DeleteView):
    model = models.Vehicle
    success_url = reverse_lazy('technic_service:vehicle_list')
    success_message = 'Aracınız basarıyla silindi.'
    template_name = 'technic_service/vehicle_delete_form.html'
    context_object_name = 'vehicle'
    success_message = 'Aracınız başarıyla silindi.'








# Kullanılan Parçalar Listesi
class PartUsageListView(generic.ListView):
    model = models.PartUsage
    template_name = 'technic_service/partusage_list.html'
    context_object_name = 'partusages'
    ordering = ['-created_at']
    queryset = models.PartUsage.objects.all()
    paginate_by = 10






# Kullanılan Parçalar Oluşturma Sayfası
class PartUsageCreateView(generic.CreateView):
    model = models.PartUsage
    form_class = forms.PartUsageForm
    success_url = reverse_lazy('technic_service:partusage_list')
    success_message = 'Kullanılan parçalarınız basarıyla oluşturuldu.'
    template_name = 'technic_service/partusage_create_form.html'
    fields = '__all__'
    context_object_name = 'partusage'








# Kullanılan Parçalar Düzenleme Sayfası
class PartUsageUpdateView(generic.UpdateView):
    model = models.PartUsage
    form_class = forms.PartUsageForm
    success_url = reverse_lazy('technic_service:partusage_list')
    success_message = 'Kullanılan parçalarınız basarıyla güncellendi.'
    template_name = 'technic_service/partusage_update_form.html'
    fields = '__all__'
    context_object_name = 'partusage'








# Kullanılan Parçalar Silme Sayfası
class PartUsageDeleteView(generic.DeleteView):
    model = models.PartUsage
    success_url = reverse_lazy('technic_service:partusage_list')
    success_message = 'Kullanılan parçalarınız basarıyla silindi.'
    template_name = 'technic_service/partusage_delete_form.html'
    context_object_name = 'partusage'






# Yedek Parçalar Listesi
class SparePartListView(generic.ListView):
    model = models.SparePart
    template_name = 'technic_service/sparepart_list.html'
    context_object_name = 'spareparts'
    ordering = ['-created_at']
    queryset = models.SparePart.objects.all()
    paginate_by = 10








# Yedek Parçalar Oluşturma Sayfası
class SparePartCreateView(generic.CreateView):
    model = models.SparePart
    form_class = forms.SparePartForm
    success_url = reverse_lazy('technic_service:sparepart_list')
    success_message = 'Yedek parçalarınız basarıyla oluşturuldu.'
    template_name = 'technic_service/sparepart_create_form.html'
    fields = '__all__'
    context_object_name = 'sparepart'








# Yedek Parçalar Düzenleme Sayfası
class SparePartUpdateView(generic.UpdateView):
    model = models.SparePart
    form_class = forms.SparePartForm
    success_url = reverse_lazy('technic_service:sparepart_list')
    success_message = 'Yedek parçalarınız basarıyla güncellendi.'
    template_name = 'technic_service/sparepart_update_form.html'
    fields = '__all__'
    context_object_name = 'sparepart'








# Yedek Parçalar Silme Sayfası
class SparePartDeleteView(generic.DeleteView):
    model = models.SparePart
    success_url = reverse_lazy('technic_service:sparepart_list')
    success_message = 'Yedek parçalarınız basarıyla silindi.'
    template_name = 'technic_service/sparepart_delete_form.html'
    context_object_name = 'sparepart'







# Servis Tipi Listesi
class ServiceTypeListView(generic.ListView):
    model = models.ServiceType
    template_name = 'technic_service/servicetype_list.html'
    context_object_name = 'servicetypes'
    ordering = ['-created_at']
    queryset = models.ServiceType.objects.all()
    paginate_by = 10






# Servis Tipi Oluşturma Sayfası
class ServiceTypeCreateView(generic.CreateView):
    model = models.ServiceType
    form_class = forms.ServiceTypeForm
    success_url = reverse_lazy('technic_service:servicetype_list')
    success_message = 'Servis tipiniz basarıyla oluşturuldu.'
    template_name = 'technic_service/servicetype_create_form.html'
    fields = '__all__'
    context_object_name = 'servicetype'






# Servis Tipi Düzenleme Sayfası
class ServiceTypeUpdateView(generic.UpdateView):
    model = models.ServiceType
    form_class = forms.ServiceTypeForm
    success_url = reverse_lazy('technic_service:servicetype_list')
    success_message = 'Servis tipiniz basarıyla güncellendi.'
    template_name = 'technic_service/servicetype_update_form.html'
    fields = '__all__'
    context_object_name = 'servicetype'






# Servis Tipi Silme Sayfası
class ServiceTypeDeleteView(generic.DeleteView):
    model = models.ServiceType
    success_url = reverse_lazy('technic_service:servicetype_list')
    success_message = 'Servis tipiniz basarıyla silindi.'
    template_name = 'technic_service/servicetype_delete_form.html'
    context_object_name = 'servicetype'





# Arac Markası Listesi
class VehicleBrandListView(generic.ListView):
    model = models.VehicleBrand
    template_name = 'technic_service/vehiclebrand_list.html'
    context_object_name = 'vehiclebrands'
    ordering = ['-created_at']
    queryset = models.VehicleBrand.objects.all()
    paginate_by = 10






# Arac Markası Oluşturma Sayfası
class VehicleBrandCreateView(generic.CreateView):
    model = models.VehicleBrand
    form_class = forms.VehicleBrandForm
    success_url = reverse_lazy('technic_service:vehiclebrand_list')
    success_message = 'Arac markanız basarıyla oluşturuldu.'
    template_name = 'technic_service/vehiclebrand_create_form.html'
    fields = '__all__'
    context_object_name = 'vehiclebrand'






# Arac Markası Düzenleme Sayfası
class VehicleBrandUpdateView(generic.UpdateView):
    model = models.VehicleBrand
    form_class = forms.VehicleBrandForm
    success_url = reverse_lazy('technic_service:vehiclebrand_list')
    success_message = 'Arac markanız basarıyla güncellendi.'
    template_name = 'technic_service/vehiclebrand_update_form.html'
    fields = '__all__'
    context_object_name = 'vehiclebrand'






# Arac Markası Silme Sayfası
class VehicleBrandDeleteView(generic.DeleteView):
    model = models.VehicleBrand
    success_url = reverse_lazy('technic_service:vehiclebrand_list')
    success_message = 'Arac markanız basarıyla silindi.'
    template_name = 'technic_service/vehiclebrand_delete_form.html'
    context_object_name = 'vehiclebrand'






# Arac Modeli Listesi
class VehicleModelListView(generic.ListView):
    model = models.VehicleModel
    template_name = 'technic_service/vehiclemodel_list.html'
    context_object_name = 'vehiclemodels'
    ordering = ['-created_at']
    queryset = models.VehicleModel.objects.all()
    paginate_by = 10






# Arac Modeli Oluşturma Sayfası
class VehicleModelCreateView(generic.CreateView):
    model = models.VehicleModel
    form_class = forms.VehicleModelForm
    success_url = reverse_lazy('technic_service:vehiclemodel_list')
    success_message = 'Arac modeliniz basarıyla oluşturuldu.'
    template_name = 'technic_service/vehiclemodel_create_form.html'
    fields = '__all__'
    context_object_name = 'vehiclemodel'






# Arac Modeli Düzenleme Sayfası
class VehicleModelUpdateView(generic.UpdateView):
    model = models.VehicleModel
    form_class = forms.VehicleModelForm
    success_url = reverse_lazy('technic_service:vehiclemodel_list')
    success_message = 'Arac modeliniz basarıyla güncellendi.'
    template_name = 'technic_service/vehiclemodel_update_form.html'
    fields = '__all__'
    context_object_name = 'vehiclemodel'






# Arac Modeli Silme Sayfası
class VehicleModelDeleteView(generic.DeleteView):
    model = models.VehicleModel
    success_url = reverse_lazy('technic_service:vehiclemodel_list')
    success_message = 'Arac modeliniz basarıyla silindi.'
    template_name = 'technic_service/vehiclemodel_delete_form.html'
    context_object_name = 'vehiclemodel'







# Yakıt Türü Oluşturma Sayfası
class FuelTypeListView(generic.ListView):
    model = models.FuelType
    template_name = 'technic_service/fueltype_list.html'
    context_object_name = 'fueltypes'
    ordering = ['-created_at']
    queryset = models.FuelType.objects.all()
    paginate_by = 10






# Yakıt Türü Oluşturma Sayfası
class FuelTypeCreateView(generic.CreateView):
    model = models.FuelType
    form_class = forms.FuelTypeForm
    success_url = reverse_lazy('technic_service:fueltype_list')
    success_message = 'Yakıt turunuz basarıyla oluşturuldu.'
    template_name = 'technic_service/fueltype_create_form.html'
    fields = '__all__'
    context_object_name = 'fueltypes'






# Yakıt Türü Düzenleme Sayfası
class FuelTypeUpdateView(generic.UpdateView):
    model = models.FuelType
    form_class = forms.FuelTypeForm
    success_url = reverse_lazy('technic_service:fueltype_list')
    success_message = 'Yakıt turunuz basarıyla güncellendi.'
    template_name = 'technic_service/fueltype_update_form.html'
    fields = '__all__'
    context_object_name = 'fueltypes'






# Yakıt Türü Silme Sayfası
class FuelTypeDeleteView(generic.DeleteView):
    model = models.FuelType
    success_url = reverse_lazy('technic_service:fueltype_list')
    success_message = 'Yakıt turunuz basarıyla silindi.'
    template_name = 'technic_service/fueltype_delete_form.html'
    context_object_name = 'fueltypes'






#  Vites Türü Oluşturma Sayfası
class TransmissionTypeListView(generic.ListView):
    model = models.TransmissionType
    template_name = 'technic_service/transmissiontype_list.html'
    context_object_name = 'transmissiontypes'
    ordering = ['-created_at']
    queryset = models.TransmissionType.objects.all()
    paginate_by = 10






#  Vites Türü Oluşturma Sayfası
class TransmissionTypeCreateView(generic.CreateView):
    model = models.TransmissionType
    form_class = forms.TransmissionTypeForm
    success_url = reverse_lazy('technic_service:transmissiontype_list')
    success_message = 'Vites turunuz basarıyla oluşturuldu.'
    template_name = 'technic_service/transmissiontype_create_form.html'
    fields = '__all__'
    context_object_name = 'transmissiontypes'







#  Vites Türü Düzenleme Sayfası
class TransmissionTypeUpdateView(generic.UpdateView):
    model = models.TransmissionType
    form_class = forms.TransmissionTypeForm
    success_url = reverse_lazy('technic_service:transmissiontype_list')
    success_message = 'Vites turunuz basarıyla güncellendi.'
    template_name = 'technic_service/transmissiontype_update_form.html'
    fields = '__all__'
    context_object_name = 'transmissiontypes'








#  Vites Türü Silme Sayfası
class TransmissionTypeDeleteView(generic.DeleteView):
    model = models.TransmissionType
    success_url = reverse_lazy('technic_service:transmissiontype_list')
    success_message = 'Vites turunuz basarıyla silindi.'
    template_name = 'technic_service/transmissiontype_delete_form.html'
    context_object_name = 'transmissiontypes'