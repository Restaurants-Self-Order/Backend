from django.contrib import admin

from .models import Shop, ShopType, ShopBranch, Country, UserBranch, Cusine

admin.site.register(Shop)
admin.site.register(ShopType)
admin.site.register(ShopBranch)
admin.site.register(Country)
admin.site.register(UserBranch)
admin.site.register(Cusine)
