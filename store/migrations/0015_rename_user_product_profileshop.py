# Generated by Django 3.2.5 on 2021-08-20 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210820_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='profileShop',
        ),
    ]
