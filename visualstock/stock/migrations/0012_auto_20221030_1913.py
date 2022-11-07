# Generated by Django 3.2.15 on 2022-10-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20221030_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='image',
            field=models.ImageField(upload_to='Images/%Y/%m/%d/601e976dbc3a44e09cf6f264445b2c40/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='principal_file',
            field=models.FileField(upload_to='StockFiles/%Y/%m/%d/15fe87d389bc48ee8ecd3c44819f41f3/', verbose_name='Archivo fuente'),
        ),
    ]