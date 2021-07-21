"""Post permissions."""

# Django REST Framework
from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsPostOwner(BasePermission):
    """Allows deleting posts only created by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user