from django.db import models
# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Stock(models.Model):
    name = models.CharField(unique=True, max_length=50, verbose_name="Nombre")
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