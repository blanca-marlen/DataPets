# Generated by Django 4.1 on 2023-02-02 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0003_remove_place_logo_height_remove_place_logo_width_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="logo",
        ),
        migrations.RemoveField(
            model_name="place",
            name="opening_hours",
        ),
        migrations.RemoveField(
            model_name="place",
            name="phone_number",
        ),
    ]
