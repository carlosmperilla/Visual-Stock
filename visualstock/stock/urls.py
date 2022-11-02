from django.urls import path

from . import views

app_name="stock"
urlpatterns = [
    path("<str:stock_name>/", views.stock, name="stock"),
    path("<str:stock_name>/edit", views.editProducts, name="editProducts"),
    path("<str:stock_name>/import_images", views.importProductImages, name="importProductImages"),
    path("<str:stock_name>/delete", views.deleteProducts, name="deleteProducts"),
]
