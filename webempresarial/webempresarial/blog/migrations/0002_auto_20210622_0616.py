# Generated by Django 3.1.4 on 2021-06-22 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created'], 'verbose_name': 'entrada', 'verbose_name_plural': 'entradas'},
        ),
    ]
