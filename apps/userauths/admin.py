from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    User,
    Profile,
    Address,
    SocialMediaProfile,
    UserPreference,
    Gender,
    Nationality,
    Job,
    Specialty,
    Duty,
    EducationLevel,
    EducationField,
    School,
    SchoolDepartment,
    Language,
    Talent,
    Hobby,
)

# Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "phone_number", "birth_date", "gender", "nationality", "identity_number", "passport_number", "job", "speciality", "duty", "place_of_work", "place_of_work_unit", "language", "hobbies", "talents", "education_level", "education_field", "school", "school_department", "graduation_year")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "is_customer", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "is_superuser", "is_customer")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ("hobbies", "talents", "groups", "user_permissions")  # Important for ManyToMany fields


# Register other models
admin.site.register(Gender)
admin.site.register(Nationality)
admin.site.register(Job)
admin.site.register(Specialty)
admin.site.register(Duty)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'profile_picture', 'website', 'location')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')  # Search by user fields

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

admin.site.register(UserPreference)
admin.site.register(EducationLevel)
admin.site.register(EducationField)
admin.site.register(School)
admin.site.register(SchoolDepartment)
admin.site.register(Language)
admin.site.register(Talent)
admin.site.register(Hobby)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "date_joined",
    )
    list_filter = ("is_active", "is_staff", "is_superuser", "gender", "job")
    search_fields = ("email", "first_name", "last_name", "phone_number")
    ordering = ("-date_joined",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone_number",
                    "birth_date",
                    "gender",
                    "nationality",
                    "identity_number",
                    "passport_number",
                )
            },
        ),
        (
            "Work info",
            {
                "fields": (
                    "job",
                    "speciality",
                    "duty",
                    "place_of_work",
                    "place_of_work_unit",
                )
            },
        ),
        (
            "Education",
            {
                "fields": (
                    "education_level",
                    "education_field",
                    "school",
                    "school_department",
                    "graduation_year",
                )
            },
        ),
        ("Additional info", {"fields": ("language", "hobbies", "talents")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_verified",
                    "is_admin",
                    "is_customer",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "location", "created_at", "updated_at")
    search_fields = ("user__email", "location")
    list_filter = ("created_at",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "country", "created_at")
    search_fields = ("user__email", "city", "country")
    list_filter = ("country", "city")


@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "platform", "created_at")
    search_fields = ("user__email", "platform")
    list_filter = ("platform", "created_at")


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ("user", "language", "theme", "receive_newsletter")
    list_filter = ("language", "theme", "receive_newsletter")
    search_fields = ("user__email",)


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("job_name", "created_at", "updated_at")
    search_fields = ("job_name",)


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(EducationField)
class EducationFieldAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(SchoolDepartment)
class SchoolDepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "school", "created_at", "updated_at")
    search_fields = ("name", "school__name")
    list_filter = ("school",)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
