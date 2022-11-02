import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete

from backup.models import Backup
from .get_products import get_and_save_products
from .receivers import (
                        delete_residual_files,
                        set_additional_column,
                        set_default_date_column_name,
                        unique_name_per_user,
                        delete_storage_files,
                        append_residual_files,
                        delete_residual_files,
                        delete_backup_files
                        )
from products.receivers import set_compressed_image

class Stock(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    image = models.ImageField(upload_to=f"Images/%Y/%m/%d/{uuid.uuid4().hex}/", max_length=100, verbose_name="Imagen")
    
    principal_file = models.FileField(upload_to=f"StockFiles/%Y/%m/%d/{uuid.uuid4().hex}/", verbose_name="Archivo fuente")
    
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
        return self.name + '-' + str(self.pk)

    def additional_column_as_list(self):
        return self.additional_column.split(',')

    def extract_products(self):
        get_and_save_products(self)

    def set_current_backup(self):
        backup = Backup(stock = self)
        backup.fill_current()
        backup.save()


pre_save.connect(set_additional_column, sender=Stock)
pre_save.connect(set_default_date_column_name, sender=Stock)
pre_save.connect(unique_name_per_user, sender=Stock)
pre_save.connect(set_compressed_image, sender=Stock)
post_delete.connect(delete_storage_files, sender=Stock)

pre_save.connect(append_residual_files, sender=Stock)
post_save.connect(delete_residual_files, sender=Stock)

pre_delete.connect(delete_backup_files, sender=Stock)