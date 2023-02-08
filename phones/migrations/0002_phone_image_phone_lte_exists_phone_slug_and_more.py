# Generated by Django 4.1.6 on 2023-02-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.URLField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=models.CharField(default='phone', max_length=50)),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(default=None, max_length=50),
        ),
    ]