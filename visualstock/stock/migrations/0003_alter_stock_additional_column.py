# Generated by Django 3.2.15 on 2022-08-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20220821_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='additional_column',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Nombres de columnas adicionales (separados por coma)'),
        ),
    ]