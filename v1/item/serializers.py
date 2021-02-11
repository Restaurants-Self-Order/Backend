from rest_framework import serializers
from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user', 'shop', 'category', 'name', 'price', 'description', 'image', 'date_added']
