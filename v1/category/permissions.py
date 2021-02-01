from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Category
from v1.shop.models import UserBranch, Shop

# check if a user has permission to Create a category
# only the shop owner or Moderator, Manager or Admin can create category
class CategoryCreate(BasePermission):

    def has_permission(self, request, view):
        flag = False
        try:
            if UserBranch.objects.filter(user=request.user, branch=request.data['branch']).exists():
                permission = UserBranch.objects.get(user=request.user, branch=request.data['branch']).permission
                if permission == 1 or permission == 2 or permission == 3:
                    flag = True
            if Shop.objects.filter(shopbranch=request.data['branch'], owner= request.user).exists():
                flag = True
        except:
            pass
        return (request.user and request.user.is_authenticated) and flag
        
class CategoryEditDelete(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) 

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view) and request.user == obj.owner