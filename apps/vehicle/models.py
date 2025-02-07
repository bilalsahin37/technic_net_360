# vehicles/models.py
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Vehicle(models.Model):
    """Araç bilgilerini tutan model"""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Araç Sahibi"),
    )
    brand = models.ForeignKey("VehicleBrand", on_delete=models.PROTECT, verbose_name=_("Marka")
    )
    model = models.ForeignKey("VehicleModel", on_delete=models.PROTECT, verbose_name=_("Model")
    )
    year = models.PositiveIntegerField(verbose_name=_("Model Yılı"))
    plate_number = models.CharField(max_length=20, unique=True, verbose_name=_("Plaka"))
    vin = models.CharField(max_length=17, unique=True, verbose_name=_("Şasi No"))
    color = models.CharField(max_length=50, verbose_name=_("Renk"))
    mileage = models.PositiveIntegerField(verbose_name=_("Kilometre"))
    fuel_type = models.ForeignKey("FuelType", on_delete=models.PROTECT, verbose_name=_("Yakıt Tipi")
    )
    transmission = models.ForeignKey("TransmissionType", on_delete=models.PROTECT, verbose_name=_("Vites Tipi")
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.model} - {self.plate_number}"

    class Meta:
        verbose_name = _("Araç")
        verbose_name_plural = _("Araçlar")
