from django.contrib import admin

from .models import Item, CustomizationGroup, CustomizationItem


admin.site.register(Item)
admin.site.register(CustomizationGroup)
admin.site.register(CustomizationItem)
