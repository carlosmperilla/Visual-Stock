from django.urls import path

from . import views

app_name="stock"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("<str:stock_name>/", views.stock, name="stock"),
]
