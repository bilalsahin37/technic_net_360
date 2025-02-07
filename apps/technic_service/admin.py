# apps/service/admin.py

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *


class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)


admin.site.register(WorkFlow, WorkFlowAdmin)


class ServiceAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "appointment_date",
        "workflow_status",
        "technician",
        "estimated_completion",
    )
    list_filter = ("appointment_date", "workflow_status", "technician")
    search_fields = ("vehicle__plate", "description")
    raw_id_fields = ("vehicle", "technician")
    date_hierarchy = "appointment_date"


admin.site.register(ServiceAppointment, ServiceAppointmentAdmin)


class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 1
    fields = ("service_type", "cost", "labor_hours", "notes")


class PartUsageInline(admin.TabularInline):
    model = PartUsage
    extra = 1
    fields = ("spare_part", "quantity", "unit_cost", "total_cost")
    readonly_fields = ("total_cost",)


class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("appointment", "completion_date", "total_cost", "warranty_end_date")
    list_filter = ("completion_date", "warranty_end_date")
    search_fields = ("appointment__vehicle__plate", "notes")
    inlines = [ServiceDetailInline, PartUsageInline]
    raw_id_fields = ("appointment",)
    date_hierarchy = "completion_date"


admin.site.register(ServiceRecord, ServiceRecordAdmin)


class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ("service_record", "service_type", "cost", "labor_hours")
    list_filter = ("service_type",)
    raw_id_fields = ("service_record",)


admin.site.register(ServiceDetail, ServiceDetailAdmin)


class PartUsageAdmin(admin.ModelAdmin):
    list_display = (
        "service_record",
        "spare_part",
        "quantity",
        "unit_cost",
        "total_cost",
    )
    list_filter = ("spare_part",)
    raw_id_fields = ("service_record", "spare_part")
    readonly_fields = ("total_cost",)


admin.site.register(PartUsage, PartUsageAdmin)


class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "standard_price", "estimated_time")
    search_fields = ("name",)
    list_filter = ("standard_price",)


admin.site.register(ServiceType, ServiceTypeAdmin)


class VehicleBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


admin.site.register(VehicleBrand, VehicleBrandAdmin)


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("brand", "name", "created_at")
    search_fields = ("brand__name", "name")
    list_filter = ("brand", "created_at")
    raw_id_fields = ("brand",)


admin.site.register(VehicleModel, VehicleModelAdmin)


class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


admin.site.register(FuelType, FuelTypeAdmin)


class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


admin.site.register(TransmissionType, TransmissionTypeAdmin)
