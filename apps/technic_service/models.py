from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User  # Eğer özel bir User modeli kullanmıyorsanız bu satırı kaldırın.

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Kullanıcı")) # ForeignKey için AUTH_USER_MODEL kullanın.
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Ad"))
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Soyad"))
    email = models.EmailField(verbose_name=_("E-Posta"), unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name=_("Telefon"), unique=True, blank=True, null=True)
    address = models.TextField(verbose_name=_("Adres"), blank=True, null=True)

    class Meta:
        verbose_name = _("Müşteri")
        verbose_name_plural = _("Müşteriler")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class WorkFlow(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("İş Akışı Durumu"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Açıklama"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncelleme Tarihi"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("İş Akışı")
        verbose_name_plural = _("İş Akışları")

class ServiceAppointment(models.Model):
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Araç"))
    appointment_date = models.DateTimeField(verbose_name=_("Randevu Tarihi"))
    description = models.TextField(verbose_name=_("Sorun Açıklaması"))
    workflow_status = models.ForeignKey(WorkFlow, on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_("Durum"))
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="assigned_appointments", verbose_name=_("Teknisyen"))
    estimated_completion = models.DateTimeField(null=True, blank=True, verbose_name=_("Tahmini Tamamlanma"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncelleme Tarihi"))

    def __str__(self):
        return f"{self.vehicle} - {self.appointment_date}"

    class Meta:
        verbose_name = _("Servis Randevusu")
        verbose_name_plural = _("Servis Randevuları")

class ServiceRecord(models.Model):
    appointment = models.ForeignKey(ServiceAppointment, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Randevu"))
    services = models.ManyToManyField('ServiceType', through='ServiceDetail', verbose_name=_("Yapılan İşlemler"))
    parts_used = models.ManyToManyField('SparePart', through='PartUsage', verbose_name=_("Kullanılan Parçalar"))
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Toplam Tutar"))
    completion_date = models.DateTimeField(default=timezone.now, blank=True, null=True, verbose_name=_("Tamamlanma Tarihi"))
    warranty_end_date = models.DateField(null=True, blank=True, verbose_name=_("Garanti Bitiş Tarihi"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notlar"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma Tarihi"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncelleme Tarihi"))

    def __str__(self):
        return f"{self.appointment.vehicle} - {self.completion_date}"

    class Meta:
        verbose_name = _("Servis Kaydı")
        verbose_name_plural = _("Servis Kayıtları")


class SparePart(models.Model):
    name = models.CharField(max_length=255)
    part_number = models.CharField(max_length=255, unique=True)
    brand = models.CharField(max_length=255)
    stock_quantity = models.PositiveIntegerField(default=0)
    min_stock_level = models.PositiveIntegerField(default=0)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    # ... other fields
    def __str__(self):
        return self.name


class ServiceDetail(models.Model):
    service_record = models.ForeignKey(ServiceRecord, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Servis Kaydı"))
    service_type = models.ForeignKey("ServiceType", on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Hizmet Tipi"))
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Ücret"))
    labor_hours = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, verbose_name=_("İşçilik Süresi"))
    notes = models.TextField(blank=True, null=True, verbose_name=_("Notlar"))

    def __str__(self):
        return f"{self.service_type} - {self.service_record}"

class Vehicle(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_("Araç Sahibi"))
    brand = models.ForeignKey("VehicleBrand", on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Marka"))
    model = models.ForeignKey("VehicleModel", on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Model"))
    year = models.PositiveIntegerField(verbose_name=_("Model Yılı"), blank=True, null=True)
    plate_number = models.CharField(max_length=20, unique=True, blank=True, null=True, verbose_name=_("Plaka"))
    vin = models.CharField(max_length=17, unique=True, blank=True, null=True, verbose_name=_("Şasi No"))
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Renk"))
    mileage = models.PositiveIntegerField(verbose_name=_("Kilometre"), blank=True, null=True)
    fuel_type = models.ForeignKey("FuelType", on_delete=models.PROTECT, verbose_name=_("Yakıt Tipi"), blank=True, null=True)
    transmission = models.ForeignKey("TransmissionType", on_delete=models.PROTECT, verbose_name=_("Vites Tipi"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate_number}"

    class Meta:
        verbose_name = _("Araç")
        verbose_name_plural = _("Araçlar")

class PartUsage(models.Model):
    service_record = models.ForeignKey(ServiceRecord, on_delete=models.CASCADE, verbose_name=_("Servis Kaydı"), related_name="part_usages", blank=True, null=True)
    spare_part = models.ForeignKey("SparePart", on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Yedek Parça"))
    quantity = models.PositiveIntegerField(verbose_name=_("Miktar"), blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Birim Fiyat"))
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Toplam Tutar"))

    def save(self, *args, **kwargs):
        if self.quantity and self.unit_cost:
            self.total_cost = self.quantity * self.unit_cost
        super().save(*args, **kwargs)
