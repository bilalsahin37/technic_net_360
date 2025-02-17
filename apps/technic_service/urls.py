from django.urls import path
from . import views

app_name = "technic_service"

urlpatterns = [
    # Customer URLs  # noqa: E501
    path("customers/", views.CustomerListView.as_view(), name="customer-list"),
    path("customers/add/", views.CustomerCreateView.as_view(), name="customer-add"),
    path("customers/<int:pk>/", views.CustomerDetailView.as_view(), name="customer-detail"),
    path(
        "customers/<int:pk>/edit/",
        views.CustomerUpdateView.as_view(),
        name="customer-edit",
    ),
    path("vehicles/<int:pk>/edit/", views.VehicleUpdateView.as_view(), name="vehicle-edit"),
    path("appointments/", views.ServiceAppointmentListView.as_view(), name="appointment-list"),
    path("appointments/add/", views.ServiceAppointmentCreateView.as_view(), name="appointment-add"),
    path("appointments/<int:pk>/", views.ServiceAppointmentDetailView.as_view(), name="appointment-detail"),
    path("appointments/<int:pk>/edit/", views.ServiceAppointmentUpdateView.as_view(), name="appointment-edit"),
]
