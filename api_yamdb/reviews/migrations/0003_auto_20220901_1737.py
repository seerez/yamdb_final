# Generated by Django 2.2.16 on 2022-09-01 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220901_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['category', 'name'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]
