from django.urls import path

from . import views

urlpatterns = [
    path("stock/", views.index, name="index"),
    path("stock/add", views.addStock, name="addStock"),
    path("stock/edit", views.editStock, name="editStock"),
    path("stock/delete", views.deleteStock, name="deleteStock"),
    path("", views.index, name="index"),
    path("stock/<str:stock_name>/export", views.stock_to_csv, name="stock_to_csv"),
]