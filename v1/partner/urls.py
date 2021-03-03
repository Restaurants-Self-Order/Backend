from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('partner', views.PartnerViewSet)
router.register('partner-application', views.PartnerApplicationViewSet)
