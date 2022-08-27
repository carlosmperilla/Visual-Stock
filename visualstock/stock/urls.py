from django.urls import path

from . import views

app_name="stock"
urlpatterns = [
        path("modal/", views.testing_modal, name="modal"),
    path("<str:stock_name>/", views.stock, name="stock"),

]
