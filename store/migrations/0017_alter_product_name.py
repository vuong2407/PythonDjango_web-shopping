# Generated by Django 3.2.5 on 2021-08-21 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_rename_profileshop_product_profile_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
