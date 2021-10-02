# Generated by Django 3.2.5 on 2021-08-20 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0003_rename_saler_profileshop_user'),
        ('store', '0013_alter_product_saler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='saler',
        ),
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saler_channel.profileshop'),
        ),
    ]
