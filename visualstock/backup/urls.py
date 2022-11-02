from django.urls import path

from . import views

app_name="backup"
urlpatterns = [
    path("<str:stock_name>/<int:backup_num>", views.toggle_backup, name="toggle_backup"),
]
