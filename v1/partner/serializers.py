from rest_framework import serializers
from .models import Partner, PartnerApplication


class PartnerSerializer(serializers.ModelSerializer):
    country = serializers.CharField(source='country.name', read_only=True)

    class Meta:
        model = Partner
        fields = ('uuid', 'first_name', 'last_name', 'email', 'phone', 'detailed_address', 'state' 'city', 'country', 'shop_name', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'


class PartnerApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerApplication
        fields = ('uuid','first_name', 'last_name', 'email', 'phone', 'designation', 'detailed_address', 'state', 'city', 'country', 'shop_name', 'number_of_branches', 'cusine', 'status', 'created_at', 'updated_at')
        read_only_fields = 'created_at', 'updated_at'
