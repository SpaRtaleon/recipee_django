# Generated by Django 4.2.3 on 2023-09-18 08:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0009_user_fav"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="img",
            field=cloudinary.models.CloudinaryField(
                max_length=255, verbose_name="category"
            ),
        ),
    ]
