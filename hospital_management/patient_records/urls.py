from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('all_patient_list', views.all_patient_list, name="all_patient_list"),
    path('patient_details/<int:pk>/', views.patient_details, name="patient_details"),
]
