# Generated by Django 3.2.5 on 2021-09-29 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
