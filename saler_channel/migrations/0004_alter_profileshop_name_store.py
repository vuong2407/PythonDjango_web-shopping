# Generated by Django 3.2.5 on 2021-08-24 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0003_rename_saler_profileshop_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileshop',
            name='name_store',
            field=models.CharField(default='', max_length=50),
        ),
    ]
