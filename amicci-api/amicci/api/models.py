from django.db import models
from django.contrib.postgres.fields import ArrayField


class Retailer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    vendors = ArrayField(models.AutoField(primary_key=True), blank=True)

    class Meta:
        app_label = 'amicci'


class Briefing(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    retailer = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)
    availabe = models.IntegerField()

    class Meta:
        app_label = 'amicci'


class Vendor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

    class Meta:
        app_label = 'amicci'


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'amicci'

