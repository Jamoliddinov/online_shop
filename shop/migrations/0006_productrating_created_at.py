# Generated by Django 3.0.3 on 2020-03-02 15:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200228_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrating',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
