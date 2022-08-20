from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.singup_user, name="signup"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
