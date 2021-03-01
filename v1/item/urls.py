from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('item', views.ItemViewSet)
router.register('customization-group', views.CustomizationGroupViewSet)
router.register('customization-item', views.CustomizationItemViewSet)
router.register('modifier-group', views.ModifierGroupViewSet)
