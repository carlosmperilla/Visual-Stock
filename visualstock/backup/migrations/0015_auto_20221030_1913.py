# Generated by Django 3.2.15 on 2022-10-30 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0014_auto_20221030_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='current',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/d34b91194de44adb8994ba8288e30028/', verbose_name='Archivo auxiliar de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='first',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/f23359c85b374fcfa88b3278f39a7cde/', verbose_name='Primer archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='first_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de primer respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='second',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/d03ee4e49353403799ba30588879e529/', verbose_name='Segundo archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='second_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de segundo respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='third',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/63be7803913c4abebefcae8a34b03005/', verbose_name='Tercer archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='third_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha de tercer respaldo'),
        ),
    ]
