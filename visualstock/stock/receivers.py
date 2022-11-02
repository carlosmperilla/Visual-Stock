import pathlib

from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage

def set_additional_column(sender, instance, *args, **kwargs):
    if not instance.additional_column:
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

def set_default_date_column_name(sender, instance, *args, **kwargs):
    if not instance.added_date_column:
        instance.added_date_column = "Fecha-Añadido"
    if not instance.updated_date_column:
        instance.updated_date_column = "Fecha-Renovado"

def unique_name_per_user(sender, instance, *args, **kwargs):
    stock_by_user = sender.objects.filter(user__pk=instance.user.pk)
    stocks_by_name = stock_by_user.filter(name=instance.name)
    if stocks_by_name.exists():
        if not instance == stocks_by_name.first():
            raise ValidationError("Nombre de Stock ya registrado previamente.")

def delete_general_file_and_folder(file, path=False):
    fs = FileSystemStorage()
    if not path:
        path_file = file.path
        file.close()
    else:
        path_file = file
    if fs.exists(path_file):
        fs.delete(path_file)
        try:
            folder_file = pathlib.Path(path_file).parent
            fs.delete(folder_file)
        except:
            pass

def delete_storage_files(sender, instance, *args, **kwargs):    
    delete_general_file_and_folder(instance.image)
    delete_general_file_and_folder(instance.principal_file)

def delete_backup_files(sender, instance, *args, **kwargs):
    if hasattr(instance, 'backup'):
        instance.backup.clean_backup_files()

def append_residual_files(sender, instance, *args, **kwargs):
    pre_instance = sender.objects.filter(pk=instance.pk).first()
    if pre_instance and (pre_instance.image != instance.image):
        instance.residual_files = [pre_instance.image]


def delete_residual_files(sender, instance, *args, **kwargs):
    if hasattr(instance, 'residual_files'):
       
        for residual_file in instance.residual_files:
            delete_general_file_and_folder(residual_file)