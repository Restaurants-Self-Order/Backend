from django.contrib import admin

from .models import Item, Cart, CartItem

admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItem)
