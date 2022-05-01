from rest_framework import permissions


class NotListOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            if not (view.action in ["list"]):
                return True
            else:
                return False
        else:
            return True
