# DRF imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

# Serializer Class imports
from .serializers import ShopSerializer, ShopBranchSerializer, CountrySerializer, CusineSerializer
from .models import Shop, ShopBranch, Country, Cusine
from .permissions import ShopEditDelete, ShopBranchCreate, ShopBranchUpdate, ShopBranchDelete


# List Of all countries
class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CusineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cusine.objects.all()
    serializer_class = CusineSerializer


# All CRUD
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), ]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            return [ShopEditDelete(), ]
        else:
            return [AllowAny(), ]


# All CRUD
class BranchViewSet(viewsets.ModelViewSet):
    queryset = ShopBranch.objects.all()
    serializer_class = ShopBranchSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [ShopBranchCreate(), ]
        elif self.action == 'update' or self.action == 'partial_update':
            return [ShopBranchUpdate(), ]
        elif self.action == 'destroy':
            return [ShopBranchDelete(), ]
        else:
            return [AllowAny(), ]

# Modified Codebase with ModelViewSet instead of writing every viewset and specifying the urls of the viewset

# class ShopCreateAPIView(CreateAPIView, GenericAPIView):
#   serializer_class = ShopSerializer

#   def perform_create(self, serializer):
#     serializer.save(owner=self.request.user)

#   permission_classes = [IsAuthenticated]

# #edit the Shop
# #only owner of the shop can edit the shop
# class ShopEditAPIView(UpdateAPIView, GenericAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     permission_classes = [ShopEditDelete]

# # delete the shop
# # only owner of the shop can delete shop
# class ShopDeleteAPIView(DestroyAPIView, GenericAPIView):
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     permission_classes = [ShopEditDelete]

# branch create view
# class BranchCreateAPIView(CreateAPIView, GenericAPIView):
#   serializer_class = ShopBranchSerializer
#   permission_classes = [ShopBranchCreate]

# # branch update view
# class BranchUpdateAPIView(UpdateAPIView, GenericAPIView):
#   queryset = ShopBranch.objects.all()
#   serializer_class = ShopBranchSerializer
#   permission_classes = [ShopBranchUpdate]

# class BranchDeleteAPIView(DestroyAPIView, GenericAPIView):
#     queryset = ShopBranch.objects.all()
#     serializer_class = ShopBranchSerializer
#     permission_classes = [ShopBranchDelete]
