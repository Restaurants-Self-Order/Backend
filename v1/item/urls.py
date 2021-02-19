from django.urls import path
from .views import items, detailsItem

urlpatterns = [
    path('', items, name='items'),
    path('detailsItem', detailsItem, name='detailsItem'),
]