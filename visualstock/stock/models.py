from django.db import models
# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Stock(models.Model):
    stock_name = models.CharField(unique=True, max_length=50, verbose_name="Nombre de Stock")
    stock_image = models.ImageField(upload_to="Images/%Y/%m/%d/", unique=True, max_length=50, verbose_name="Imagen de Stock")
    stock_file = models.FileField(upload_to="StockFiles/%Y/%m/%d/", unique=True, verbose_name="Archivo del Stock")
    
    product_name_col = models.CharField(unique=True, max_length=50, verbose_name="Columna de nombre-producto")
    price_col = models.CharField(unique=True, max_length=50, verbose_name="Columna precio")
    amount_col = models.CharField(unique=True, max_length=50, verbose_name="Columna cantidad")
    categories_col = models.CharField(default=None, unique=True, max_length=50, verbose_name="Columna categorias")
    added_date_col = models.CharField(default=None, unique=True, max_length=50, verbose_name="Columna de fecha-añadido")
    renewal_date_col = models.CharField(default=None, unique=True, max_length=50, verbose_name="Columna de fecha-renovado")
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Nuevos Stocks"
        ordering = ['stock_name']

    def __str__(self):
        return self.stock_name