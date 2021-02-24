from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(trailing_slash=False)
router.register('category', views.CategoryViewSet)
router.register('menu', views.MenuViewSet)
router.register('menu-category', views.MenuCategoryViewSet)