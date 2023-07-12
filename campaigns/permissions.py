from rest_framework import permissions

class LoggedInAndReadOnly(permissions.BasePermission):
    """
    Custom permission:
        - Allow full access for authenticated users
        - Allow read-only access for unauthenticated users
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user.is_authenticated  # Allow other operations if user is authenticated

class IsAuthenticatedAndIsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj == request.user
