
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from v1.shop.urls import router as shop_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

router = DefaultRouter(trailing_slash=False)

router.registry.extend(shop_router.registry)
urlpatterns += router.urls
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)