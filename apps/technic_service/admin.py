from django.contrib import admin
from .models import (
    Customer,
    WorkFlow,
    ServiceAppointment,
    ServiceRecord,
    ServiceDetail,
    Vehicle,
    PartUsage,
    SparePart,
    ServiceType,
    VehicleBrand,
    VehicleModel,
    FuelType,
    TransmissionType,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("first_name", "last_name")


@admin.register(WorkFlow)
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("created_at", "updated_at")


@admin.register(ServiceAppointment)
class ServiceAppointmentAdmin(admin.ModelAdmin):
    list_display = ("vehicle", "appointment_date", "workflow_status", "technician")
    search_fields = ("vehicle__plate_number", "technician__username")
    list_filter = ("appointment_date", "workflow_status")


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("appointment", "total_cost", "completion_date", "warranty_end_date")
    search_fields = ("appointment__vehicle__plate_number",)
    list_filter = ("completion_date", "warranty_end_date")


@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ("service_record", "service_type", "cost", "labor_hours")
    search_fields = (
        "service_record__appointment__vehicle__plate_number",
        "service_type__name",
    )
    list_filter = ("service_type",)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ("brand", "model", "year", "plate_number", "vin", "owner")
    search_fields = ("plate_number", "vin", "owner__username")
    list_filter = ("brand", "model", "year", "fuel_type", "transmission")


@admin.register(PartUsage)
class PartUsageAdmin(admin.ModelAdmin):
    list_display = (
        "service_record",
        "spare_part",
        "quantity",
        "unit_cost",
        "total_cost",
    )
    search_fields = (
        "service_record__appointment__vehicle__plate_number",
        "spare_part__name",
    )
    list_filter = ("spare_part",)


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("name", "part_number", "brand", "stock_quantity", "selling_price")
    search_fields = ("name", "part_number", "brand")
    list_filter = ("brand",)


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "standard_price", "estimated_time")
    search_fields = ("name",)
    list_filter = ("standard_price",)


@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ("brand", "name")
    search_fields = ("name", "brand__name")
    list_filter = ("brand",)


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(TransmissionType)
class TransmissionTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
