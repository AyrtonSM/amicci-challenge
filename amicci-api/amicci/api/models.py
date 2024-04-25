from django.db import models
from django.contrib.postgres.fields import ArrayField


class Retailer(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    vendors = ArrayField(models.CharField(max_length=50), blank=True, default=list)


class Briefing(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
    retailer = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    release_date = models.CharField(max_length=50)
    availabe = models.IntegerField()


class Vendor(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)


class Category(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=200)
