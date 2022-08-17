from django.urls import path

from . import views

urlpatterns = [
    path("stock/", views.index, name="index"),
    path("", views.index, name="index"),
]