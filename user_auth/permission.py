from django.contrib.auth.models import Group
from rest_framework import permissions

def _is_in_group(user_auth, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_auth_set.filter(id=user_auth.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user_auth, required_groups):
    return any([_is_in_group(user_auth, group_name) for group_name in required_groups])


class IsLoggedInUserAuthOrAdmin(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user_auth, self.required_groups)
        if self.required_groups is None:
            return False
        return obj == request.user_auth or has_group_permission

class IsAdminUser(permissions.BasePermission):
    # group_name for super admin
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user_auth, self.required_groups)
        return request.user_auth and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(request.user_auth, self.required_groups)
        return request.user_auth and has_group_permission


class IsAdminOrAnonymousUser(permissions.BasePermission):
    required_groups = ['admin', 'anonymous']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user_auth, self.required_groups)
        return request.user_auth and has_group_permission
