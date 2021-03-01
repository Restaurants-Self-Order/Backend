from rest_framework import serializers

from .models import Item, CustomizationGroup, CustomizationItem, ModifierGroup


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

class CustomizationGroupCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomizationGroup
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'


class CustomizationGroupUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomizationGroup
        fields = ('uuid', 'name', 'required', 'min_select', 'max_select')
        read_only_fields = 'created_at', 'updated_at'


class CustomizationItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomizationItem
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'


class ModifierGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModifierGroup
        fields = ('__all__')
        read_only_fields = 'created_at', 'updated_at'
