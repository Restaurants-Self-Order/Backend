from rest_framework import serializers
from .models import Category
from v1.shop.models import ShopBranch

class CategorySerializer(serializers.ModelSerializer):
  branch = serializers.PrimaryKeyRelatedField(queryset=ShopBranch.objects.all())

  class Meta:
    model = Category
    fields = ('branch', 'name')