from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.singup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
