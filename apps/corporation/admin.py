from django.contrib import admin
from .models import Corporation, Unit, SubUnit


@admin.register(Corporation)
class CorporationAdmin(admin.ModelAdmin):
    list_display = ("name", "corporation_number", "created_at", "updated_at")
    search_fields = ("name", "corporation_number")
    list_filter = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_per_page = 20
    ordering = ("-created_at",)


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "unit_number", "corporation", "created_at", "updated_at")
    search_fields = ("name", "unit_number", "corporation__name")
    list_filter = ("corporation", "created_at", "updated_at")
    date_hierarchy = "created_at"
    list_per_page = 20
    ordering = ("-created_at",)
    autocomplete_fields = ["corporation"]  # Auto-complete for corporation search


@admin.register(SubUnit)
class SubUnitAdmin(admin.ModelAdmin):
    list_display = ("name", "sub_unit_number", "unit", "corporation", "created_at", "updated_at")
    search_fields = ("name", "sub_unit_number", "unit__name")
    list_filter = ("unit", "created_at", "updated_at")
    date_hierarchy = "created_at"
    list_per_page = 20
    ordering = ("-created_at",)
    autocomplete_fields = ["unit"]
