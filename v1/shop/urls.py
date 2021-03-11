from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('branch', views.BranchViewSet)
router.register('shop', views.ShopViewSet)
# Api for country list
router.register('country', views.CountryViewSet)
# Api for cusine list
router.register('cusine', views.CusineViewSet)
