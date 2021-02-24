from rest_framework.permissions import BasePermission

from v1.shop.models import UserBranch, Shop

from .models import Category, Menu


# check if a user has permission to Create a category
# only the shop owner or Moderator, Manager or Admin can create category
class ItemCreate(BasePermission):

    def has_permission(self, request, view):
        flag = False
        if request.data.get('branch'):
            if UserBranch.objects.filter(user=request.user, branch=request.data['branch']).exists():
                permission = UserBranch.objects.get(user=request.user, branch=request.data['branch']).permission
                if permission == 1 or permission == 2 or permission == 3:
                    flag = True
            if Shop.objects.filter(shopbranch=request.data['branch'], owner=request.user).exists():
                flag = True
        return (request.user and request.user.is_authenticated) and flag


class ItemUpdate(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        flag = False
        if UserBranch.objects.filter(user=request.user, branch=obj.branch).exists():
            permission = UserBranch.objects.get(user=request.user, branch=obj.branch).permission
            if permission == 2 or permission == 3:
                flag = True
        if Shop.objects.filter(shopbranch=obj.branch, owner=request.user).exists():
            flag = True
        return request.user and request.user.is_authenticated and flag


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