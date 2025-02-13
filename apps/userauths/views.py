from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . import models
from . import forms



# Kullanıcı Kayıt Sayfası
class UserCreateView(generic.CreateView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_form.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    success_message = "Kayıt oluşturuldu."






# Kullanıcı Güncelleme Sayfası
class UserUpdateView(generic.UpdateView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_form.html"
    form_class = forms.UserUpdateForm
    success_url = reverse_lazy("home")
    # fields = ["username", "email"]  # Güncellenecek alanları belirtiyoruz.
    fields = "__all__"  # Tüm alanları güncellemek istiyorsak bu şekilde kullanabiliriz.






# Kullanıcı Silme Sayfası
class UserDeleteView(generic.DeleteView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_confirm_delete.html"
    success_url = reverse_lazy("home")







# Kullanıcı Listeleme Sayfası
class UserListView(generic.ListView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_list.html"
    context_object_name = "users"
    ordering = ["-date_joined"]
    paginate_by = 10
    queryset = models.User.objects.all()
    # queryset = models.User.objects.filter(is_staff=True)  # Yetkili kullanıcıları listeye almak istiyorsak bu şekilde kullanabiliriz.





class UserDetailView(generic.DetailView):
    model = settings.AUTH_USER_MODEL
    template_name = "registration/user_detail.html"
    context_object_name = "user"
    # fields = ["username", "email"]  # Görünücek alanları belirtiyoruz.
    fields = "__all__"  # Tüm alanları göstermek istiyorsak bu şekilde kullanabiliriz.