from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.dashboard, name="dashboard"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("patient/", views.patient, name="patient"),
]
