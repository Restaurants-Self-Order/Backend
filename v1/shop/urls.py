from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('branch', views.BranchViewSet)
router.register('shop', views.ShopViewSet)
