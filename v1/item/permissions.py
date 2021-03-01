from rest_framework.permissions import BasePermission

from v1.shop.models import UserBranch, Shop
from v1.item.models import Item

from .models import Category, Menu, CustomizationGroup


class MenuCategoryPermission(BasePermission):
    def has_permission(self, request, view):
        user_has_perm = False
        item_in_branch = False
        if request.data.get('branch') and request.data.get('category') and request.data.get('menu'):
            if UserBranch.objects.filter(user=request.user, branch=request.data['branch']).exists():
                permission = UserBranch.objects.get(user=request.user, branch=request.data['branch']).permission
                if permission == 1 or permission == 2 or permission == 3:
                    user_has_perm = True
            elif Shop.objects.filter(shopbranch=request.data['branch'], owner=request.user).exists():
                user_has_perm = True

            if Category.objects.filter(uuid=request.data['category'], branch=request.data['branch']).exists() and \
               Menu.objects.filter(uuid=request.data['menu'], branch=request.data['branch']).exists():
                item_in_branch = True

        return (request.user and request.user.is_authenticated) and user_has_perm and item_in_branch


class CustomizationItemPermission(BasePermission):
    
    def has_permission(self, request, view):
        user_has_permission = False
        item_in_branch = False
        if request.data.get('branch') and request.data.get('customization_group') and request.data.get('item'):
            if UserBranch.objects.filter(user=request.user, branch=request.data['branch']).exists():
                permission = UserBranch.objects.get(user=request.user, branch=request.data['branch']).permission
                if permission == 1 or permission == 2 or permission == 3:
                    user_has_perm = True
            elif Shop.objects.filter(shopbranch=request.data['branch'], owner=request.user).exists():
                user_has_perm = True

            if Item.objects.filter(uuid=request.data['item'], branch=request.data['branch']).exists() and \
               CustomizationGroup.objects.filter(uuid=request.data['menu'], branch=request.data['branch']).exists():
                item_in_branch = True

        return (request.user and request.user.is_authenticated) and user_has_perm and item_in_branch