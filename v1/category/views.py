from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS

from .models import Category, Menu, MenuCategory, ItemCategory
from .serializers import CategoryCreateSerializer, CategoryUpdateSerializer, MenuCreateSerializer, MenuUpdateSerializer, MenuCategorySerializer
from .permissions import ItemCreate, ItemUpdate, MenuCategoryPermission


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return CategoryCreateSerializer
        return CategoryUpdateSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()

    def get_serializer_class(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return MenuCreateSerializer
        return MenuUpdateSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [MenuCategoryPermission(), ]
