# Generated by Django 3.2.5 on 2021-08-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_auto_20210825_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
