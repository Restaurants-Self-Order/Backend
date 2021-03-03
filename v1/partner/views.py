from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from v1.third_party.rest_framework.permissions import IsStaff

from .models import Partner, PartnerApplication
from .serializers import PartnerSerializer, PartnerApplicationSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsStaff]


class PartnerApplicationViewSet(viewsets.ModelViewSet):
    queryset = PartnerApplication.objects.all()
    serializer_class = PartnerApplicationSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(), ]
        else:
            return [IsStaff(), ]
