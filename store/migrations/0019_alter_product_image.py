# Generated by Django 3.2.5 on 2021-08-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='product_images'),
        ),
    ]
