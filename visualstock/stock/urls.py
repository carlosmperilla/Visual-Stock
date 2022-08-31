from django.urls import path

from . import views

app_name="stock"
urlpatterns = [
    path("<str:stock_name>/", views.stock, name="stock"),
]
