from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.singup_user, name="signup"),
    path("renew_captcha/", views.renew_captcha, name="renew_captcha"),
    path("review_captcha/", views.review_captcha, name="review_captcha"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]
