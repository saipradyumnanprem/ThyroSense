from django.urls import path
from . import views

urlpatterns = [
    path("user", views.user_dashboard, name="user_dashboard"),
    path("add_report/", views.add_report, name="add_report"),
    path("report/", views.user_report, name="user_report"),
    # path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("user_profile/", views.user_profile, name="user_profile"),

]
