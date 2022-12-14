# Generated by Django 3.2.15 on 2022-10-30 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20221029_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='image',
            field=models.ImageField(upload_to='Images/%Y/%m/%d/c5cf90ff610b4a3791c0e6e837131e77/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='principal_file',
            field=models.FileField(upload_to='StockFiles/%Y/%m/%d/3553297ce0ad4e94a4e027b238e4f949/', verbose_name='Archivo fuente'),
        ),
    ]
