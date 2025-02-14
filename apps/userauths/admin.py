from django.contrib import admin
from .models import (
    User, Gender, Nationality, Job, Speciality, Duty, Profile, Address,
    SocialMediaProfile, UserPreference, EducationLevel, EducationField,
    School, SchoolDepartment, Language, Talent, Hobby
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('email',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'description')
    search_fields = ('job_name', 'description')

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'biography', 'website', 'location')
    search_fields = ('user__email', 'biography', 'website', 'location')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'street', 'city', 'state', 'postal_code', 'country')
    search_fields = ('user__email', 'street', 'city', 'state', 'postal_code', 'country')

@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')
    search_fields = ('user__email', 'platform', 'url')

@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'theme', 'receive_newsletter')
    search_fields = ('user__email', 'language', 'theme')

@admin.register(EducationLevel)
class EducationLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(EducationField)
class EducationFieldAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(SchoolDepartment)
class SchoolDepartmentAdmin(admin.ModelAdmin):
    list_display = ('school', 'name')
    search_fields = ('school__name', 'name')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
