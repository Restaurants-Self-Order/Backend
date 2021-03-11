from rest_framework import serializers
from v1.partner.models import PartnerApplication

class WeeklGraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerApplication
        fields = '__all__'
    
