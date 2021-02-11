from rest_framework.permissions import BasePermission
from v1.shop.models import UserBranch, Shop


# check if a user has permission to Create a category
# only the shop owner or Moderator, Manager or Admin can create category
class CategoryCreate(BasePermission):

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


class CategoryEditDelete(BasePermission):

    def has_permission(self, request, view):
        flag = False
        if request.data.get('branch'):
            if UserBranch.objects.filter(user=request.user, branch=request.data['branch']).exists():
                permission = UserBranch.objects.get(user=request.user, branch=request.data['branch']).permission
                if permission == 2 or permission == 3:
                    flag = True
            if Shop.objects.filter(shopbranch=request.data['branch'], owner=request.user).exists():
                flag = True
        return request.user and request.user.is_authenticated and flag
