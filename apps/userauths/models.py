from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.base_user import BaseUserManager
from datetime import date

from apps.corporation.models import Corporation, Unit


# Ortak zaman damgası alanları için soyut model
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Oluşturulma Tarihi")
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("Güncellenme Tarihi")
    )

    class Meta:
        abstract = True


# Özel Kullanıcı Yöneticisi
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


# Optimize Edilmiş Custom User Model
class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    email = models.EmailField(
        unique=True,
        max_length=100,
        help_text=_("User's email address."),
        verbose_name=_("E-posta"),
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text=_("Primary phone number."),
        verbose_name=_("Telefon Numarası"),
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("User's first name."),
        verbose_name=_("İsim"),
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("User's last name."),
        verbose_name=_("Soyisim"),
    )
    birth_date = models.DateField(
        blank=True,
        null=True,
        help_text=_("User's birth date."),
        verbose_name=_("Doğum Tarihi"),
    )
    gender = models.ForeignKey(
        "Gender",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's gender."),
        verbose_name=_("Cinsiyet"),
    )
    nationality = models.ForeignKey(
        "Nationality",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's nationality."),
        verbose_name=_("Uyruk"),
    )
    identity_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("User's identity number."),
        verbose_name=_("Kimlik Numarası"),
    )
    passport_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text=_("User's passport number."),
        verbose_name=_("Pasaport Numarası"),
    )
    job = models.ForeignKey(
        "Job",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's job."),
        verbose_name=_("Meslek"),
    )
    speciality = models.ForeignKey(
        "Speciality",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's speciality."),
        verbose_name=_("Uzmanlık"),
    )
    duty = models.ForeignKey(
        "Duty",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's duty."),
        verbose_name=_("Görev"),
    )
    place_of_work = models.ForeignKey(
        Corporation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's place of work."),
        verbose_name=_("Çalışma Yeri"),
    )
    place_of_work_unit = models.ForeignKey(
        Unit,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's place of work department."),
        verbose_name=_("Departman"),
    )
    language = models.ForeignKey(
        "Language",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's language."),
        verbose_name=_("Dil"),
    )
    hobbies = models.ManyToManyField(
        "Hobby", help_text=_("User's hobbies."), verbose_name=_("Hobiler")
    )
    talents = models.ManyToManyField(
        "Talent", help_text=_("User's talents."), verbose_name=_("Yetenekler")
    )
    education_level = models.ForeignKey(
        "EducationLevel",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's education level."),
        verbose_name=_("Eğitim Seviyesi"),
    )
    education_field = models.ForeignKey(
        "EducationField",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's education field."),
        verbose_name=_("Eğitim Alanı"),
    )
    school = models.ForeignKey(
        "School",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's school."),
        verbose_name=_("Okul"),
    )
    school_department = models.ForeignKey(
        "SchoolDepartment",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text=_("User's school department."),
        verbose_name=_("Okul Departmanı"),
    )
    graduation_year = models.IntegerField(
        blank=True, null=True, verbose_name=_("Son eğitim yılı")
    )
    is_verified = models.BooleanField(default=False, verbose_name=_("Onaylı mı?"))
    is_active = models.BooleanField(default=True, verbose_name=_("Aktif mi?"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Sahip mi?"))
    is_admin = models.BooleanField(default=False, verbose_name=_("Yönetici mi?"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Personel mi?"))
    is_customer = models.BooleanField(default=False, verbose_name=_("Müşteri mi?"))

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            return (
                today.year
                - self.birth_date.year
                - (
                    (today.month, today.day)
                    < (self.birth_date.month, self.birth_date.day)
                )
            )
        return None

    def __str__(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

    class Meta:
        verbose_name = _("Kullanıcı")
        verbose_name_plural = _("Kullanıcılar")
        ordering = ["email"]


# Destekleyici Modeller (TimeStampedModel'dan türetiliyor)
class Gender(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Cinsiyet Adı"),
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Cinsiyet")
        verbose_name_plural = _("Cinsiyetler")


class Nationality(TimeStampedModel):
    name = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name=_("Uyruk Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Uyruk")
        verbose_name_plural = _("Uyruklar")


class Job(TimeStampedModel):
    job_name = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name=_("Meslek Adı")
    )
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name=_("Açıklama")
    )

    def __str__(self):
        return self.job_name or ""

    class Meta:
        verbose_name = _("Meslek")
        verbose_name_plural = _("Meslekler")


class Speciality(TimeStampedModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name=_("Uzmanlık Adı"),
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Uzmanlık")
        verbose_name_plural = _("Uzmanlıklar")


class Duty(TimeStampedModel):
    name = models.CharField(
        max_length=100, unique=True, blank=True, null=True, verbose_name=_("Görev Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Görev")
        verbose_name_plural = _("Görevler")


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name=_("Kullanıcı"),
    )
    biography = models.TextField(blank=True, null=True, verbose_name=_("Biyografi"))
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True,
        verbose_name=_("Profil Resmi"),
    )
    website = models.URLField(blank=True, null=True, verbose_name=_("Web Sitesi"))
    location = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Konum")
    )

    def __str__(self):
        return f"Profile of {self.user.email}"

    class Meta:
        verbose_name = _("Profil")
        verbose_name_plural = _("Profiller")


class Address(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses",
        verbose_name=_("Kullanıcı"),
    )
    street = models.CharField(
        max_length=255, blank=True, null=True, verbose_name=_("Sokak")
    )
    city = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Şehir")
    )
    state = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Eyalet")
    )
    postal_code = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Posta Kodu")
    )
    country = models.CharField(
        max_length=100, blank=True, null=True, verbose_name=_("Ülke")
    )

    def __str__(self):
        return f"Address for {self.user.email}"

    class Meta:
        verbose_name = _("Adres")
        verbose_name_plural = _("Adresler")


class SocialMediaProfile(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="social_profiles",
        verbose_name=_("Kullanıcı"),
    )
    platform = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Platform")
    )
    url = models.URLField(blank=True, null=True, verbose_name=_("Profil Linki"))

    def __str__(self):
        return f"{self.platform} profile for {self.user.email}"

    class Meta:
        verbose_name = _("Sosyal Profil")
        verbose_name_plural = _("Sosyal Profiller")


class UserPreference(TimeStampedModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="preferences",
        verbose_name=_("Kullanıcı"),
    )
    language = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default="tr",
        verbose_name=_("Dil Tercihi"),
    )
    theme = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        default="light",
        verbose_name=_("Tema Tercihi"),
    )
    receive_newsletter = models.BooleanField(
        default=True, verbose_name=_("Bülten Alıyor mu?")
    )

    def __str__(self):
        return f"Preferences for {self.user.email}"

    class Meta:
        verbose_name = _("Kullanıcı Tercihi")
        verbose_name_plural = _("Kullanıcı Tercihleri")


class EducationLevel(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Eğitim Seviyesi Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Eğitim Seviyesi")
        verbose_name_plural = _("Eğitim Seviyeleri")


class EducationField(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Eğitim Alanı Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Eğitim Alanı")
        verbose_name_plural = _("Eğitim Alanları")


class School(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Okul Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Okul")
        verbose_name_plural = _("Okullar")


class SchoolDepartment(TimeStampedModel):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Okul")
    )
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Okul Departmanı Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Okul Departmanı")
        verbose_name_plural = _("Okul Departmanları")


class Language(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Dil Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Dil")
        verbose_name_plural = _("Diller")


class Talent(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Yetenek Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Yetenek")
        verbose_name_plural = _("Yetenekler")


class Hobby(TimeStampedModel):
    name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name=_("Hobi Adı")
    )

    def __str__(self):
        return self.name or ""

    class Meta:
        verbose_name = _("Hobi")
        verbose_name_plural = _("Hobiler")
