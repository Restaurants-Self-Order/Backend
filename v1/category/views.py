from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer
from .permissions import CategoryCreate, CategoryEditDelete

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [CategoryCreate(), ] 
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [CategoryEditDelete(), ] 
        else :
            return [CategoryEditDelete(), ] 