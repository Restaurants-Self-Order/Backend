from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from v1.third_party.rest_framework.permissions import IsStaff

from .models import Partner, PartnerApplication
from .serializers import PartnerSerializer, PartnerApplicationSerializer, PartnerApplicationCreateSerializer

# create, list, details, update and delete Partner
class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsStaff]


# create, list, details, update and delete appliaction form
class PartnerApplicationViewSet(viewsets.ModelViewSet):
    queryset = PartnerApplication.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(), ]
        else:
            return [IsStaff(), ]

    def get_serializer_class(self):
        print(self.request.data)
        if self.request.method == 'create':
            return PartnerApplicationCreateSerializer
        else:
            return PartnerApplicationSerializer
