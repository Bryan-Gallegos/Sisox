# Generated by Django 3.2.4 on 2021-07-15 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_usuarios_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='codigo',
        ),
        migrations.AddField(
            model_name='usuarios',
            name='dni',
            field=models.IntegerField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]
