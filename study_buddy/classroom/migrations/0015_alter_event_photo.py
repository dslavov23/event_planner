# Generated by Django 4.1.4 on 2022-12-15 21:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0014_remove_event_event_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
