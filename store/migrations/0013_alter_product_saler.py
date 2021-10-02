# Generated by Django 3.2.5 on 2021-08-20 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0002_alter_profileshop_name_store'),
        ('store', '0012_product_saler'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='saler',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_related_shop', to='saler_channel.profileshop'),
        ),
    ]
