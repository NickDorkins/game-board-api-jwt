from rest_framework import permissions
import rest_framework

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.creator is None:
            return True

        return obj.creator == request.user
