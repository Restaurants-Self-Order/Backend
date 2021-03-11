from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
# create, list, details, update and delete Partner
router.register('partner', views.PartnerViewSet)
# create, list, details, update and delete appliaction form
router.register('partner-application', views.PartnerApplicationViewSet)
