from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Profile,
    Address,
    SocialMediaProfile,
    UserPreference,
    Gender,
    Nationality,
    Job,
    Speciality,
    Duty,
    EducationLevel,
    EducationField,
    School,
    SchoolDepartment,
    Language,
    Talent,
    Hobby,
)


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


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
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
