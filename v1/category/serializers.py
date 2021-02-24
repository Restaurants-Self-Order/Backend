from rest_framework import serializers

from .models import Category, Menu
from v1.shop.models import ShopBranch


class CategorySerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

    class Meta:
        model = Category
        fields = ('branch', 'name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at', 'branch'


class MenuSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

    class Meta:
        model = Menu
        fields = ('name', 'start_time', 'end_time', 'branch', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at', 'branch'
