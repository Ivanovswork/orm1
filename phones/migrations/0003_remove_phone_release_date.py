# Generated by Django 4.1.6 on 2023-02-08 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_phone_image_phone_lte_exists_phone_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='release_date',
        ),
    ]
