# Generated by Django 3.2.15 on 2022-10-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='Images/%Y/%m/%d/2d408fa3f0bf4ffd987d4ca2b6a7f504/', verbose_name='Imagen'),
        ),
    ]
