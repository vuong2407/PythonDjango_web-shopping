# Generated by Django 3.2.5 on 2021-08-25 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0006_alter_profileshop_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileshop',
            name='name_store',
            field=models.CharField(blank=True, default='YourNameShop...', max_length=50, null=True),
        ),
    ]
