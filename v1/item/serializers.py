from rest_framework import serializers
from .models import Item


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'

class ItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('')
        read_only_fields = 'created_at', 'updated_at'
