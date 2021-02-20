from rest_framework import viewsets

from .models import Partner
from v1.third_party.rest_framework.permissions import IsStaff
from rest_framework.permissions import AllowAny
from .serializers import PartnerSerializer, PartnerCreateSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return PartnerSerializer
        return PartnerCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(), ]
        else:
            return [IsStaff(), ]
