from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Partner
        fields = ('uuid', 'name', 'street_address', 'city', 'country', 'first_name',
                  'last_name', 'email', 'phone', 'status', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class PartnerApplicationSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', read_only=True)
    cusine = serializers.CharField(source='cusine.name', read_only=True)

    class Meta:
        model = Partner
        fields = ('uuid', 'name', 'street_address', 'city', 'country', 'first_name',
                  'last_name', 'email', 'phone', 'cusine', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'
