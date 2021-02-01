from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter(trailing_slash=False)
router.register('category', views.CategoryViewSet)