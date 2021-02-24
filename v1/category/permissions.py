from rest_framework.permissions import BasePermission
from v1.shop.models import UserBranch, Shop


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
