from django.db import models
from django.utils.translation import gettext_lazy as _


class Corporation(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Kurum Adı"
    )
    corporation_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Kurum Numarası"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Kurumlar"
        verbose_name = "Kurum"

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Birim Adı"
    )
    unit_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Birim Numarası"
    )
    corporation = models.ForeignKey(
        Corporation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Kurum",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Birimler"
        verbose_name = "Birim"

    def __str__(self):
        return self.name


class SubUnit(models.Model):
    name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Alt Birim Adı"
    )
    sub_unit_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Alt Birim Numarası"
    )
    corporation = models.ForeignKey(
        Corporation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Kurum",
    )
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Birim"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Alt Birimler"
        verbose_name = "Alt Birim"

    def __str__(self):
        return self.name


class VehicleBrand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Marka Adı"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Araç Markası")
        verbose_name_plural = _("Araç Markaları")

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    brand = models.ForeignKey(
        VehicleBrand, on_delete=models.CASCADE, verbose_name=_("Marka")
    )
    name = models.CharField(max_length=100, verbose_name=_("Model"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Model")
        verbose_name_plural = _("Modeller")

    def __str__(self):
        return f"{self.brand} {self.name}"
