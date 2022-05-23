from rest_framework.permissions import BasePermission

SAFE_METHODS_MY = ('GET', 'HEAD', 'OPTIONS')


class MyPermissions(BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS_MY or
            request.user.is_staff or request.user.is_moderator
        )
