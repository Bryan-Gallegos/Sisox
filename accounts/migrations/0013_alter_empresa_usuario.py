# Generated by Django 3.2.4 on 2021-07-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_dni_empresa_dniempresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='usuario',
            field=models.CharField(max_length=75),
        ),
    ]
