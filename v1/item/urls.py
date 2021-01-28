from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name="api-overview"),
  # category apis
  path('category', views.CategoryList.as_view() , name="category-list"),
  path('category/<str:pk>', views.categoryDetail, name="category-detail"),
  path('category/add', views.categoryCreate, name="category-create"),
  path('category/<str:pk>/edit', views.categoryUpdate, name="category-update"),
  path('category/<str:pk>/delete', views.categoryDelete, name="category-delete"),
  # Item apis
  path('item', views.ItemList.as_view(), name="item-list"),
  path('item/<str:pk>', views.itemDetail, name="item-detail"),
  path('item/add', views.itemCreate, name="item-create"),
  path('item/<str:pk>/edit', views.itemUpdate, name="item-update"),
  path('item/<str:pk>/delete', views.itemDelete, name="item-delete"),
]
