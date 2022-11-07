# Generated by Django 3.2.15 on 2022-10-29 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0005_auto_20221028_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='current',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/06826ec8248e48b4b55a7de9d13655a6/', verbose_name='Archivo auxiliar de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='first',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/0e14540ce56a49378b43ea5c059c9894/', verbose_name='Primer archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='second',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/5609031af71346da8d7508d980fbaf05/', verbose_name='Segundo archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='third',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/ee998a01cc0644a7859bc9cbf02b48e4/', verbose_name='Tercer archivo de respaldo'),
        ),
    ]