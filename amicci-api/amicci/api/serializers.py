from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = ['id', 'name', 'retailer', 'responsible', 'category', 'release_date', 'availabe']


class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = ['id', 'name', 'vendors']