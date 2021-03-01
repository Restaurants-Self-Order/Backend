from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from .models import Item, CustomizationGroup, CustomizationItem
from .serializers import ItemCreateSerializer, ItemUpdateSerializer, CustomizationGroupCreateSerializer, CustomizationGroupUpdateSerializer
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


class CustomizationGroupViewSet(viewsets.ModelViewSet):
    queryset = CustomizationGroup.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return CustomizationGroupCreateSerializer
        return CustomizationGroupUpdateSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]

class CustomizationItemViewSet(viewsets.ModelViewSet):
    queryset = CustomizationItem.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return CustomizationGroupCreateSerializer
        return CustomizationGroupUpdateSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            return [ItemCreate()(), ]
        else:
            return [ItemUpdate(), ]
