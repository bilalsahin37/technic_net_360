from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from . import models
from . import forms


# Kurum Listeleme Sayfası
class CorporationListView(generic.ListView):
    model = models.Corporation
    template_name = 'corporation/corporation_list.html'
    context_object_name = 'corporations'
    ordering = '-created_at'
    queryset = models.Corporation.objects.all()
    paginate_by = 10






# Kurum Ekleme Sayfası
class CorporationCreateView(generic.CreateView):
    model = models.Corporation
    template_name = 'corporation/corporation_create.html'
    form_class = forms.CorporationForm
    success_url = reverse_lazy('corporation: corporation_list')  # Kurum listesi sayfasına yönlendirildir






# Kurum Düzenleme Sayfası
class CorporationUpdateView(generic.UpdateView):
    model = models.Corporation
    template_name = 'corporation/corporation_update.html'
    form_class = forms.CorporationForm
    success_url = reverse_lazy('corporation: corporation_list')
    success_message = 'Kurum basarıyla güncellendi.'
    context_object_name = 'corporation'






# Kurum Silme Sayfası
class CorporationDeleteView(generic.DeleteView):
    model = models.Corporation
    template_name = 'corporation/corporation_delete.html'
    success_url = reverse_lazy('corporation: corporation_list')
    success_message = 'Kurum basarıyla silindi.'
    context_object_name = 'corporation'







class CorporationDetailView(generic.DetailView):
    model = models.Corporation
    template_name = 'corporation/corporation_detail.html'
    context_object_name = 'corporation'
    





# Birim Listeleme Sayfası
class UnitListView(generic.ListView):
    model = models.Unit
    template_name = 'corporation/unit_list.html'
    context_object_name = 'units'
    ordering = '-created_at'
    paginate_by = 10






# Birim Ekleme Sayfası
class UnitCreateView(generic.CreateView):
    model = models.Unit
    template_name = 'corporation/unit_create.html'
    form_class = forms.UnitForm
    success_url = reverse_lazy('corporation: unit_list')  # Birim listesi sayfasına yönlendirildir
    success_message = 'Birim basarıyla oluşturuldu.'






# Birim Düzenleme Sayfası
class UnitUpdateView(generic.UpdateView):
    model = models.Unit
    template_name = 'corporation/unit_update.html'
    form_class = forms.UnitForm
    success_url = reverse_lazy('corporation: unit_list')
    success_message = 'Birim basarıyla güncellendi.'
    context_object_name = 'unit'






class UnitDetailView(generic.DetailView):
    model = models.Unit
    template_name = 'corporation/unit_detail.html'
    context_object_name = 'unit'







# Birim Silme Sayfası
class UnitDeleteView(generic.DeleteView):
    model = models.Unit 
    template_name = 'corporation/unit_delete.html'
    success_url = reverse_lazy('corporation: unit_list')
    success_message = 'Birim basarıyla silindi.'
    context_object_name = 'unit'





# Alt Departman Listeleme Sayfası
class SubUnitListView(generic.ListView):
    model = models.SubUnit
    template_name = 'corporation/subunit_list.html'
    context_object_name = 'subunits'
    ordering = '-created_at'
    paginate_by = 10







# Alt Departman Ekleme Sayfası
class SubUnitCreateView(generic.CreateView):
    model = models.SubUnit
    template_name = 'corporation/subunit_create.html'
    form_class = forms.SubUnitForm
    success_url = reverse_lazy('corporation: subunit_list')  # Birim listesi sayfasına yönlendirildir
    success_message = 'Alt Birim basarıyla oluşturuldu.'
    context_object_name ='subunit'







class SubUnitUpdateView(generic.UpdateView):
    model = models.SubUnit
    template_name = 'corporation/subunit_update.html'
    form_class = forms.SubUnitForm
    success_url = reverse_lazy('corporation: subunit_list')
    success_message = 'Alt Birim basarıyla güncellendi.'
    context_object_name = 'subunit'






class SubUnitDetailView(generic.DetailView):
    model = models.SubUnit
    template_name = 'corporation/subunit_detail.html'
    context_object_name = 'subunit'







class SubUnitDeleteView(generic.DeleteView):
    model = models.SubUnit 
    template_name = 'corporation/subunit_delete.html'
    success_url = reverse_lazy('corporation: subunit_list')
    success_message = 'Alt Birim basarıyla silindi.'
    context_object_name = 'subunit'










