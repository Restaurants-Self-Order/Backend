from django.contrib import admin

from .models import Category, ItemCategory, MenuCategory, Menu

admin.site.register(Category)
admin.site.register(ItemCategory)
admin.site.register(MenuCategory)
admin.site.register(Menu)
