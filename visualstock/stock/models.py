from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import pre_save

from django.core.exceptions import ValidationError

class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    image = models.ImageField(upload_to="Images/%Y/%m/%d/", max_length=100, verbose_name="Imagen")
    principal_file = models.FileField(upload_to="StockFiles/%Y/%m/%d/", verbose_name="Archivo fuente")
    first_backup_file = models.FileField(null=True, default="NULL", upload_to="StockFiles/%Y/%m/%d/", verbose_name="Primer archivo de respaldo")
    second_backup_file = models.FileField(null=True, default="NULL", upload_to="StockFiles/%Y/%m/%d/", verbose_name="Segundo archivo de respaldo")
    third_backup_file = models.FileField(null=True, default="NULL", upload_to="StockFiles/%Y/%m/%d/", verbose_name="Tercer archivo de respaldo")
    
    name_column = models.CharField(max_length=50, verbose_name="Columna de nombre-producto")
    price_column = models.CharField(max_length=50, verbose_name="Columna precio")
    quantity_column = models.CharField(max_length=50, verbose_name="Columna cantidad")
    category_column = models.CharField(blank=True, default="", max_length=50, verbose_name="Columna categorias")
    added_date_column = models.CharField(blank=True, default="", max_length=50, verbose_name="Columna de fecha-añadido")
    updated_date_column = models.CharField(blank=True, default="", max_length=50, verbose_name="Columna de fecha-renovado")
    additional_column = models.TextField(blank=True, default="", max_length=500, verbose_name="Nombres de columnas adicionales, separados por coma")
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"
        ordering = ['name']

    def __str__(self):
        return self.name

def set_additional_column(sender, instance, *args, **kwargs):
    column_types = ["name_column",
                    "price_column",
                    "quantity_column",
                    "category_column",
                    "added_date_column",
                    "updated_date_column"]
    column_names = instance.principal_file.readline().decode('utf-8').strip().split(',')
    instance.principal_file.seek(0)
    
    for column_type in column_types:
        column_value = getattr(instance, column_type)
        if column_value != "":
            column_names.remove(column_value)

    instance.additional_column = ",".join(column_names)

def unique_name_per_user(sender, instance, *args, **kwargs):
    stock_by_user = Stock.objects.filter(user__pk=instance.user.pk)
    stocks_by_name = stock_by_user.filter(name=instance.name)
    n_stocks_by_name = stocks_by_name.count()
    if n_stocks_by_name > 0:
        if not instance == stocks_by_name.first():
            raise ValidationError("Nombre de Stock ya registrado previamente.")


pre_save.connect(set_additional_column, sender=Stock)
pre_save.connect(unique_name_per_user, sender=Stock)