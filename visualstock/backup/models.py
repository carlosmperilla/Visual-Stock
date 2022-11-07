import uuid, json

from django.db import models

from django.db.models.signals import pre_save, post_save, post_delete
from django.core import serializers
from django.core.files.base import ContentFile
from django.utils import timezone

from stock.receivers import delete_general_file_and_folder

class Backup(models.Model):
    current = models.FileField(null=True, default="NULL", upload_to=f"BackupFiles/%Y/%m/%d/{uuid.uuid4().hex}/", verbose_name="Archivo auxiliar de respaldo") 
    first = models.FileField(null=True, default="NULL", upload_to=f"BackupFiles/%Y/%m/%d/{uuid.uuid4().hex}/", verbose_name="Primer archivo de respaldo")
    second = models.FileField(null=True, default="NULL", upload_to=f"BackupFiles/%Y/%m/%d/{uuid.uuid4().hex}/", verbose_name="Segundo archivo de respaldo")
    third = models.FileField(null=True, default="NULL", upload_to=f"BackupFiles/%Y/%m/%d/{uuid.uuid4().hex}/", verbose_name="Tercer archivo de respaldo")

    first_date = models.DateTimeField(null=True, verbose_name='Fecha de primer respaldo')
    second_date = models.DateTimeField(null=True, verbose_name='Fecha de segundo respaldo')
    third_date = models.DateTimeField(null=True, verbose_name='Fecha de tercer respaldo')

    stock = models.OneToOneField('stock.Stock', null=True, editable=True, verbose_name='Stocks', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Respaldo"
        verbose_name_plural = "Respaldos"

    def __str__(self):
       return "Respaldo-" + self.stock.name + "-" +str(self.stock.pk)

    def fill_current(self):
        """
            Generates the json corresponding to the current product status and saves it in its corresponding field.
        """
        current_state = serializers.serialize('json', self.stock.products.all())
        backup_name = f"Respaldo-{self.stock.name}-{self.stock.pk}.json"
        backup_file = ContentFile(current_state, name=backup_name)
        self.current = backup_file

    def remove_residual_files(self, old_backup):
        """
            Delete the oldest and most unusable backup files.
        """
        if old_backup != "NULL":
            old_backup_list = json.loads(old_backup.read().decode('utf-8', errors='ignore'))
            last_backup_list = json.loads(self.first.read().decode('utf-8', errors='ignore'))
            old_backup.close()
            self.first.close()
            old_images = {product['fields']['image'] for product in old_backup_list if product['fields']['image'] != ""}
            last_images = {product['fields']['image'] for product in last_backup_list if product['fields']['image'] != ""}
            removable_images = old_images - last_images
            for path_image in removable_images:
                delete_general_file_and_folder(path_image, path=True)
            delete_general_file_and_folder(old_backup)

    def rotate_backup(self):
        """
            Rotate the backs. 
            The first is stored to delete. 
            The second to the first. 
            The third to the second. 
            The current state to the third. 
            The current state is stored, 
            residual files from the oldest backup are deleted. 
            And the dates are updated.
        """
        old_backup = self.first

        self.first = self.second
        self.first_date = self.second_date
        self.second = self.third
        self.second_date = self.third_date
        self.third = self.current
        self.third_date = timezone.now()
        
        self.fill_current()
        self.remove_residual_files(old_backup)
        self.save()

    def clean_backup_files(self):
        """
            Delete the backups and the files corresponding to the backups.
        """
        backups = [self.current, self.first, self.second, self.third]
    
        img_residual = set()
        for backup in backups:
            if backup == "NULL":
                continue
            try:
                backup_list = json.loads(backup.read().decode('utf-8', errors='ignore'))
                backup_imgs = {product['fields']['image'] for product in backup_list if product['fields']['image'] != ""}
                img_residual.update(backup_imgs)
                delete_general_file_and_folder(backup)
                backup.close()
            except FileNotFoundError:
                pass
        
        for path_image in img_residual:
            delete_general_file_and_folder(path_image, path=True)
        
    

