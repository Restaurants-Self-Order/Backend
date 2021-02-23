from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'user', 'shop', 'category', 'name', 'price', 'description', 'image', 'date_added']
        read_only_fields = 'created_at', 'updated_at'