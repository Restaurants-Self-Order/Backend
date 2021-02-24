from django.contrib import admin

from .models import Item, CustomizationGroup, CustomizationItem, Currency, ModifierGroup


admin.site.register(Item)
admin.site.register(CustomizationGroup)
admin.site.register(CustomizationItem)
admin.site.register(Currency)
admin.site.register(ModifierGroup)
