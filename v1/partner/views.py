from rest_framework import viewsets

from .models import Partner
from v1.third_party.rest_framework.permissions import IsStaff
from .serializers import PartnerSerializer


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [IsStaff]
