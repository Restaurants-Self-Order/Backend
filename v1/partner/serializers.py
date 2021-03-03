from rest_framework import serializers
from .models import Partner, PartnerApplication


class PartnerSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Partner
        fields = ('uuid', 'name', 'street_address', 'city', 'country', 'first_name',
                  'last_name', 'email', 'phone', 'status', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class PartnerApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerApplication
        fields = ('uuid', 'name', 'street_address', 'city', 'country', 'first_name',
                  'last_name', 'email', 'phone', 'cusine', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'
