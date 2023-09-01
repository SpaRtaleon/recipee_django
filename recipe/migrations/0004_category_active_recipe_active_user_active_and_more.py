# Generated by Django 4.2.3 on 2023-08-20 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0003_rename_fullname_user_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="category", name="active", field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="recipe", name="active", field=models.BooleanField(default=0),
        ),
        migrations.AddField(
            model_name="user", name="active", field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
