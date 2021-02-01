from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Shop, UserBranch, ShopBranch

# check if a user has permission to edit a shop
# only the owner can edit/ delete or create shop branch
class ShopEditDelete(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) and \
            (request.method == 'PATCH' or request.method == 'DELETE')

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view) and request.user == obj.owner

# check if a user has permission to create a shop branch
# only the owner of the shop can create another branch
class ShopBranchCreate(BasePermission):

    def has_permission(self, request, view):
        flag = False
        if request.data.get('shop'):
            if Shop.objects.get(id=request.data['shop']).owner == request.user:
                flag = True
        return (request.user and request.user.is_authenticated) and flag
    
# check if a user has permission to edit a shop branch
# shop owner or the user with admin permission of that branch can edit the shop branch
class ShopBranchUpdate(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        flag = False
        if UserBranch.objects.filter(user=request.user, branch=obj).exists():
            permission = UserBranch.objects.get(user=request.user, branch=obj).permission
            if permission == 3:
                flag = True
        if Shop.objects.filter(shopbranch=obj, owner= request.user).exists():
            flag = True
        return self.has_permission(request, view) and flag
    
# check if a user has permission to delete a shop branch
# only the owner of the shop can delete the branch
class ShopBranchDelete(BasePermission):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) and request.method == 'DELETE'
        
    def has_object_permission(self, request, view, obj):
        """Object level permission, allow editing self"""
        return self.has_permission(request, view) and request.user == obj.shop.owner
