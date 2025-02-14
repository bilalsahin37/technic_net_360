from django.urls import path
from .views import (
    CorporationCreateView,
    CorporationUpdateView,
    CorporationDeleteView,
    CorporationListView,
    UnitCreateView,
    UnitUpdateView,
    UnitDeleteView,
    UnitListView,
    SubUnitCreateView,
    SubUnitUpdateView,
    SubUnitDeleteView,
    SubUnitListView,
)

urlpatterns = [
    # Corporation URLs
    path("corporations/", CorporationListView.as_view(), name="corporation_list"),
    path(
        "corporation/add/", CorporationCreateView.as_view(), name="corporation_create"
    ),
    path(
        "corporation/<int:pk>/edit/",
        CorporationUpdateView.as_view(),
        name="corporation_update",
    ),
    path(
        "corporation/<int:pk>/delete/",
        CorporationDeleteView.as_view(),
        name="corporation_delete",
    ),
    # Unit URLs
    path("units/", UnitListView.as_view(), name="unit_list"),
    path("unit/add/", UnitCreateView.as_view(), name="unit_create"),
    path("unit/<int:pk>/edit/", UnitUpdateView.as_view(), name="unit_update"),
    path("unit/<int:pk>/delete/", UnitDeleteView.as_view(), name="unit_delete"),
    # SubUnit URLs
    path("subunits/", SubUnitListView.as_view(), name="subunit_list"),
    path("subunit/add/", SubUnitCreateView.as_view(), name="subunit_create"),
    path("subunit/<int:pk>/edit/", SubUnitUpdateView.as_view(), name="subunit_update"),
    path(
        "subunit/<int:pk>/delete/", SubUnitDeleteView.as_view(), name="subunit_delete"
    ),
]
