# Generated by Django 4.1 on 2022-10-01 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_editor',
            field=models.BooleanField(default=False),
        ),
    ]
