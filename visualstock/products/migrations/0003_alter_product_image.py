# Generated by Django 3.2.15 on 2022-10-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='Images/%Y/%m/%d/91d0530c4db44317b963bc810fc5fef5/', verbose_name='Imagen'),
        ),
    ]
