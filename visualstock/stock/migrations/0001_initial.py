# Generated by Django 3.2.15 on 2022-10-28 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='Images/%Y/%m/%d/9b842aa4c9fc41c586851c6384cd7180/', verbose_name='Imagen')),
                ('principal_file', models.FileField(upload_to='StockFiles/%Y/%m/%d/2497f80e98df4ca3b36284191ed421c8/', verbose_name='Archivo fuente')),
                ('name_column', models.CharField(max_length=50, verbose_name='Columna de nombre-producto')),
                ('price_column', models.CharField(max_length=50, verbose_name='Columna precio')),
                ('quantity_column', models.CharField(max_length=50, verbose_name='Columna cantidad')),
                ('category_column', models.CharField(blank=True, default='', max_length=50, verbose_name='Columna categorias')),
                ('added_date_column', models.CharField(blank=True, default='', max_length=50, verbose_name='Columna de fecha-añadido')),
                ('updated_date_column', models.CharField(blank=True, default='', max_length=50, verbose_name='Columna de fecha-renovado')),
                ('additional_column', models.TextField(blank=True, default='', max_length=500, verbose_name='Nombres de columnas adicionales, separados por coma')),
                ('products_generates', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stocks',
                'ordering': ['name'],
            },
        ),
    ]
