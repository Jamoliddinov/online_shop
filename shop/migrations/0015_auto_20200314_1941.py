# Generated by Django 3.0.3 on 2020-03-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200314_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcolor',
            name='color_en',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='color_ru',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='color_uz',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
