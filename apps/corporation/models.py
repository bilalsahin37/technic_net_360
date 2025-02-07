from django.db import models

class Corporation(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kurum Adı")
    corporation_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kurum Numarası")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Kurumlar'
        verbose_name = 'Kurum'

    def __str__(self):
        return self.name






class Unit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Birim Adı")
    unit_number = models.CharField(max_length=100, blank=True, null=True, verbose_name="Birim Numarası")
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kurum")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name_plural = 'Departmanlar'
        verbose_name = 'Departman'

    def __str__(self):
        return self.name





