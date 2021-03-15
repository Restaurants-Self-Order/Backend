from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)

# Api for country list
router.register('country', views.CountryViewSet)
# Api for cusine list
router.register('cusine', views.CusineViewSet)
# Api for shop CRUD
router.register('shop', views.ShopViewSet)
# Api for shop-branch CRUD
router.register('branch', views.BranchViewSet)


