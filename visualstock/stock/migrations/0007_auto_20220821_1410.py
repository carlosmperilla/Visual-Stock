# Generated by Django 3.2.15 on 2022-08-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_alter_stock_first_backup_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='first_backup_file',
            field=models.FileField(default='NULL', null=True, upload_to='StockFiles/%Y/%m/%d/', verbose_name='Primer archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='second_backup_file',
            field=models.FileField(default='NULL', null=True, upload_to='StockFiles/%Y/%m/%d/', verbose_name='Segundo archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='third_backup_file',
            field=models.FileField(default='NULL', null=True, upload_to='StockFiles/%Y/%m/%d/', verbose_name='Tercer archivo de respaldo'),
        ),
    ]