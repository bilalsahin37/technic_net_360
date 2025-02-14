from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Corporation, Unit, SubUnit


# Corporation Views
class CorporationCreateView(CreateView):
    model = Corporation
    fields = ["name", "corporation_number"]
    template_name = "corporation_form.html"
    success_url = reverse_lazy("corporation_list")


class CorporationUpdateView(UpdateView):
    model = Corporation
    fields = ["name", "corporation_number"]
    template_name = "corporation_form.html"
    success_url = reverse_lazy("corporation_list")


class CorporationDeleteView(DeleteView):
    model = Corporation
    template_name = "corporation_confirm_delete.html"
    success_url = reverse_lazy("corporation_list")


class CorporationListView(ListView):
    model = Corporation
    template_name = "corporation_list.html"
    context_object_name = "corporations"


# Unit Views
class UnitCreateView(CreateView):
    model = Unit
    fields = ["name", "unit_number", "corporation"]
    template_name = "unit_form.html"
    success_url = reverse_lazy("unit_list")


class UnitUpdateView(UpdateView):
    model = Unit
    fields = ["name", "unit_number", "corporation"]
    template_name = "unit_form.html"
    success_url = reverse_lazy("unit_list")


class UnitDeleteView(DeleteView):
    model = Unit
    template_name = "unit_confirm_delete.html"
    success_url = reverse_lazy("unit_list")


class UnitListView(ListView):
    model = Unit
    template_name = "unit_list.html"
    context_object_name = "units"


# SubUnit Views
class SubUnitCreateView(CreateView):
    model = SubUnit
    fields = ["name", "sub_unit_number", "corporation", "unit"]
    template_name = "subunit_form.html"
    success_url = reverse_lazy("subunit_list")


class SubUnitUpdateView(UpdateView):
    model = SubUnit
    fields = ["name", "sub_unit_number", "corporation", "unit"]
    template_name = "subunit_form.html"
    success_url = reverse_lazy("subunit_list")


class SubUnitDeleteView(DeleteView):
    model = SubUnit
    template_name = "subunit_confirm_delete.html"
    success_url = reverse_lazy("subunit_list")


class SubUnitListView(ListView):
    model = SubUnit
    template_name = "subunit_list.html"
    context_object_name = "subunits"
