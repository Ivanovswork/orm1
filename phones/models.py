from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=50, null=False, default='phone')
    price = models.CharField(max_length=50, default=None)
    image = models.URLField(max_length=100, null=False, default=None)
    release_date = models.CharField(max_length=50, null=False, default=None)
    lte_exists = models.CharField(max_length=50, null=False, default=None)
    slug = models.SlugField(max_length=50, null=False, default=name)
