# Generated by Django 3.2.15 on 2022-10-28 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0003_auto_20221028_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backup',
            name='first',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/2a8c58bbb84b42049828b852b66e200c/', verbose_name='Primer archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='hidden',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/0d875d2890cc4ccbb38d6c0e1215a564/', verbose_name='Archivo auxiliar de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='second',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/bfe73be2dadd40a79dcf321bf9a0beb6/', verbose_name='Segundo archivo de respaldo'),
        ),
        migrations.AlterField(
            model_name='backup',
            name='third',
            field=models.FileField(default='NULL', null=True, upload_to='BackupFiles/%Y/%m/%d/8d0ed5ad3dd840cbb92dffd971162699/', verbose_name='Tercer archivo de respaldo'),
        ),
    ]
