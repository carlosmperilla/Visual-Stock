# Generated by Django 3.2.15 on 2022-08-14 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['stock_name'], 'verbose_name': 'Stock', 'verbose_name_plural': 'Nuevos Stocks'},
        ),
        migrations.RemoveField(
            model_name='stock',
            name='user',
        ),
        migrations.AlterField(
            model_name='stock',
            name='amount_col',
            field=models.CharField(max_length=50, unique=True, verbose_name='Columna cantidad'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_col',
            field=models.CharField(max_length=50, unique=True, verbose_name='Columna precio'),
        ),
    ]