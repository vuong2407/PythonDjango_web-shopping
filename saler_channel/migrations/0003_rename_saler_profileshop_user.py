# Generated by Django 3.2.5 on 2021-08-20 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saler_channel', '0002_alter_profileshop_name_store'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileshop',
            old_name='saler',
            new_name='user',
        ),
    ]
