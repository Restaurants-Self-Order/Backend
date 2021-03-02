from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from .models import Item, CustomizationGroup, CustomizationItem, ModifierGroup
from .serializers import ItemCreateSerializer, ItemUpdateSerializer, CustomizationGroupCreateSerializer, \
    CustomizationGroupUpdateSerializer, ModifierGroupSerializer, CustomizationItemSerializer
from .permissions import ModifierGroupPermission

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
            return CustomizationItemSerializer
        return CustomizationItemSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]


class ModifierGroupViewSet(viewsets.ModelViewSet):
    queryset = ModifierGroup.objects.all()
    serializer_class = ModifierGroupSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'destroy':
            return [ModifierGroupPermission(), ]
        else:
            return [ModifierGroupPermission(), ]
