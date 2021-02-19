
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from v1.shop.urls import router as shop_router
from v1.category.urls import router as category_router
from v1.partner.urls import router as partner_router
#for django views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # Item Urls
    path('items/', include('v1.item.urls')),
]

router = DefaultRouter(trailing_slash=False)
router.registry.extend(shop_router.registry)
router.registry.extend(category_router.registry)
router.registry.extend(partner_router.registry)
urlpatterns += router.urls
