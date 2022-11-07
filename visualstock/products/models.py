from tabnanny import verbose
import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save

from .receivers import (
                        set_product_availability,
                        set_unique_slug,
                        set_compressed_image
                        )


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name="Nombre unico de producto")
    image = models.ImageField(null=True, upload_to=f"Images/%Y/%m/%d/{uuid.uuid4().hex}/", max_length=100, verbose_name="Imagen")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Precio")
    quantity = models.IntegerField(verbose_name="Cantidad", validators=[MinValueValidator(-99999999), MaxValueValidator(99999999)])
    category = models.CharField(blank=True, default="", max_length=50, verbose_name="Categoria")

    additional = models.TextField(blank=True, default="", max_length=500, verbose_name="Datos adicionales en orden, separados por comas.")

    available = models.BooleanField(default=True, verbose_name="¿Esta disponible?")
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Editado el')
        
    stock = models.ForeignKey('stock.Stock', editable=True, verbose_name='Stock', on_delete=models.CASCADE, related_name="products")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.slug

    def additional_as_list(self):
        """
            Splits the string of additional dnd returns their list.
        """
        return self.additional.split(',')


pre_save.connect(set_product_availability, sender=Product)
pre_save.connect(set_unique_slug, sender=Product)
pre_save.connect(set_compressed_image, sender=Product)