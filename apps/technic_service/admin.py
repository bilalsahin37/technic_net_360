from django.contrib import admin
from .models import (
    Customer,
    WorkFlow,
    ServiceAppointment,
    ServiceRecord,
    SparePart,
    ServiceDetail,
    Vehicle,
    PartUsage,
)


# ServiceRecord modelinde ilişkilendirilen alt modeller için inlines
class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 0


class PartUsageInline(admin.TabularInline):
    model = PartUsage
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "first_name", "last_name", "email", "phone")
    search_fields = ("first_name", "last_name", "email", "phone")
    list_filter = ("user",)


@admin.register(WorkFlow)
class WorkFlowAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(ServiceAppointment)
class ServiceAppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "vehicle",
        "appointment_date",
        "workflow_status",
        "technician",
        "estimated_completion",
    )
    search_fields = ("vehicle__plate_number",)
    list_filter = ("workflow_status", "technician")


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("appointment", "total_cost", "completion_date", "warranty_end_date")
    search_fields = ("appointment__vehicle__plate_number",)
    inlines = [ServiceDetailInline, PartUsageInline]


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("name", "part_number", "brand", "stock_quantity", "selling_price")
    search_fields = ("name", "part_number", "brand")


@admin.register(ServiceDetail)
class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ("service_record", "service_type", "cost", "labor_hours")
    search_fields = ("service_record__appointment__vehicle__plate_number",)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "brand",
        "model",
        "year",
        "plate_number",
        "vin",
        "color",
        "mileage",
    )
    search_fields = ("plate_number", "vin", "brand__name", "model__name")
    list_filter = ("brand", "model", "year")


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
