from rest_framework import viewsets

from .models import Partner
from v1.third_party.rest_framework.permissions import IsStaff
from rest_framework.permissions import AllowAny
from .serializers import PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsStaff]

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        else:
            return [IsStaff(), ]
