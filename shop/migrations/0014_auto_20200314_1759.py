# Generated by Django 3.0.3 on 2020-03-14 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20200313_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrating',
            name='description_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='description_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='description_uz',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='title_uz',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
