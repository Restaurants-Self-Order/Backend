from rest_framework import serializers

from .models import Category, Menu
from v1.shop.models import ShopBranch
from v1.shop.serializers import ShopBranchSerializer


class CategoryCreateSerializer(serializers.ModelSerializer):
    branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

    class Meta:
        model = Category
        fields = ('uuid', 'branch', 'name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at', 'branch'

class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('uuid', 'name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at', 'branch'


class MenuCreateSerializer(serializers.ModelSerializer):

    branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

    class Meta:
        model = Menu
        fields = ('uuid', 'name', 'start_time', 'end_time', 'branch', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'

class MenuUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('uuid', 'name', 'start_time', 'end_time', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'
