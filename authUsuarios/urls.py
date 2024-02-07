from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome,name="authU_welcome"),
    path("signup/", views.signup,name="authU_signup")
]