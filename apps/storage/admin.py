from django.contrib import admin

from .models import SparePart


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "part_number",
        "brand",
        "stock_quantity",
        "min_stock_level",
        "purchase_price",
        "selling_price",
        "location",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "part_number", "brand")
    list_filter = ("brand", "location")
    ordering = ("name",)
    date_hierarchy = "created_at"
    empty_value_display = "-Boş-"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "part_number",
                    "brand",
                    "compatible_models",
                    "description",
                )
            },
        ),
        (
            "Stock Information",
            {
                "fields": (
                    "stock_quantity",
                    "min_stock_level",
                    "purchase_price",
                    "selling_price",
                    "location",
                )
            },
        ),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )
