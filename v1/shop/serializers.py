from rest_framework import serializers

from .models import Shop, ShopBranch, Country, Cusine

from v1.category.serializers import MenuUpdateSerializer, CategoryUpdateSerializer


class ShopBranchSerializer(serializers.ModelSerializer):

    menu = MenuUpdateSerializer(source='menu_set', many=True, read_only=True)
    category = CategoryUpdateSerializer(source='category_set', many=True, read_only=True)

    class Meta:
        model = ShopBranch
        fields = ('uuid', 'title', 'street_address', 'city',
                  'country', 'region', 'state', 'postal_code', 'latitude',
                  'longitude', 'description', 'opening_time', 'closing_time', 'menu', 'category')


class ShopSerializer(serializers.ModelSerializer):

    shop = ShopBranchSerializer(source='shopbranch_set', many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('uuid', 'name', 'image', 'shop')


# to register partner, filter shop, shopbranch items
class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('__all__')

#  to register partner, filter shop
class CusineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cusine
        fields = ('__all__')
