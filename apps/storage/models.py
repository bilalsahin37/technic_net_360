from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.vehicle.models import Vehicle


class SparePart(models.Model):
    """Yedek parça bilgilerini tutan model"""

    name = models.CharField(max_length=200, verbose_name=_("Parça Adı"))
    part_number = models.CharField(
        max_length=50, unique=True, verbose_name=_("Parça Numarası")
    )
    brand = models.CharField(max_length=100, verbose_name=_("Marka"))
    compatible_models = models.ManyToManyField(
        Vehicle, verbose_name=_("Uyumlu Modeller")
    )
    stock_quantity = models.PositiveIntegerField(verbose_name=_("Stok Miktarı"))
    min_stock_level = models.PositiveIntegerField(
        verbose_name=_("Minimum Stok Seviyesi")
    )
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Alış Fiyatı")
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Satış Fiyatı")
    )
    location = models.CharField(max_length=50, verbose_name=_("Depo Konumu"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Açıklama"))
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Oluşturulma Tarihi")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Güncelleme Tarihi")
    )

    def __str__(self):
        return f"{self.name} - {self.part_number}"

    class Meta:
        verbose_name = _("Yedek Parça")
        verbose_name_plural = _("Yedek Parçalar")
