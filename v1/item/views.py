# DRF imports
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets

# Serializer Class imports
from .models import Item, CustomiztionGroup, Customization_Items
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404


# Items
def items(request):
    items = Item.objects.all()
    return render(request, 'item.html', {'items': items})

def detailsItem(request):
    item = get_object_or_404(Item, uuid="8f4bcf2e5c6d486abec7cf49ebefdf71")
    return render(request, 'detailsItem.html', { 'item': item })

