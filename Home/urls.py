from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="index"),
    path("patient-login/", views.patient_login, name="login_page"),
    path("doctor-login/", views.doctor_login, name="doctor_login"),
    path("doctor-dashboard/", views.doctor_dashboard, name="doctor_dashboard"),
    path("patient-signup/", views.patient_signup, name="signup_page"),
    path("logout/", views.logout_page, name="logout_page"),
    # path("community/", views.community, name="user_blog")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
