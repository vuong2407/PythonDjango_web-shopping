# Generated by Django 3.2.5 on 2021-08-20 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileshop',
            name='name_store',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
