# Generated by Django 3.2.15 on 2022-08-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='Images/%Y/%m/%d/', verbose_name='Imagen'),
        ),
    ]
