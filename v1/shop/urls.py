from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter(trailing_slash=False)
router.register('branch', views.BranchViewSet)
router.register('shop', views.ShopViewSet)

# urlpatterns = [
#   path('add/', views.ShopCreateAPIView.as_view(), name="create-shop"),
#   path('<str:pk>/edit/', views.ShopEditAPIView.as_view(), name="edit-shop"),
#   path('<str:pk>/delete/', views.ShopDeleteAPIView.as_view(), name="delete-shop"),
#   path('branch/add/', views.BranchCreateAPIView.as_view(), name="create-branch"),
#   path('branch/<str:pk>/edit/', views.BranchUpdateAPIView.as_view(), name="edit-branch"),
#   path('branch/<str:pk>/delete/', views.BranchDeleteAPIView.as_view(), name="delete-branch"),
# ]