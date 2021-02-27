from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, IsAdminUser

from .models import Item
from .serializers import ItemCreateSerializer, ItemUpdateSerializer
from v1.category.permissions import ItemCreate, ItemUpdate

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return ItemCreateSerializer
        return ItemUpdateSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]
