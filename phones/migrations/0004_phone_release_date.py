# Generated by Django 4.1.6 on 2023-02-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_remove_phone_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
