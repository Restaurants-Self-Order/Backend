from rest_framework import viewsets
from rest_framework.permissions import AllowAny, SAFE_METHODS

from .models import Category, Menu
from .serializers import CategorySerializer, MenuSerializer
from .permissions import ItemCreate, ItemUpdate


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action == 'create' or self.request.method in SAFE_METHODS:
            return [ItemCreate(), ]
        else:
            return [ItemUpdate(), ]
