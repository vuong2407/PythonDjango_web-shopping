# Generated by Django 3.2.5 on 2021-08-20 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_product_saler'),
        ('user', '0004_delete_itemsaler'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Saler',
        ),
    ]
