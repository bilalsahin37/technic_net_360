from django.contrib import admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 20
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('name', 'created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')
    save_on_top = True
    save_as = True
    save_as_continue = False
    
