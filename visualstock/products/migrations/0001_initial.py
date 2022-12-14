# Generated by Django 3.2.15 on 2022-10-28 04:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stock', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('slug', models.SlugField(unique=True, verbose_name='Nombre unico de producto')),
                ('image', models.ImageField(null=True, upload_to='Images/%Y/%m/%d/1a7e4e1008a548a286a40446a5e927c3/', verbose_name='Imagen')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(-99999999), django.core.validators.MaxValueValidator(99999999)], verbose_name='Cantidad')),
                ('category', models.CharField(blank=True, default='', max_length=50, verbose_name='Categoria')),
                ('additional', models.TextField(blank=True, default='', max_length=500, verbose_name='Datos adicionales en orden, separados por comas.')),
                ('available', models.BooleanField(default=True)),
                ('added_date', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Editado el')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='stock.stock', verbose_name='Stock')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['name'],
            },
        ),
    ]
