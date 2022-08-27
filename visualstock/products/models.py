from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.db.models.signals import pre_save
from stock.models import Stock

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name="Nombre unico de producto")
    image = models.ImageField(null=True, upload_to="Images/%Y/%m/%d/", max_length=100, verbose_name="Imagen")

    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(verbose_name="Cantidad", validators=[MinValueValidator(-99999999), MaxValueValidator(99999999)])
    category = models.CharField(blank=True, default="", max_length=50, verbose_name="Categoria")

    additional = models.TextField(blank=True, default="", max_length=500, verbose_name="Datos adicionales en orden, separados por comas.")

    available = models.BooleanField(default=True)
    added_date = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Editado el')
        
    stock = models.ForeignKey(Stock, editable=True, verbose_name='Stock', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

def set_product_not_avaliable(sender, instance, *args, **kwargs):
    if instance.quantity <= 0:
        instance.avaliable = False

pre_save.connect(set_product_not_avaliable, sender=Product)