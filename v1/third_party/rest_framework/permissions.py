from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    """The request is authenticated as a user and is staff, or is a read-only request"""

    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsStaff(BasePermission):
    """The request has only permission to be used by the staff """

    def has_permission(self, request, view):
        return (request.user and request.user.is_staff) and request.method != 'DELETE'
