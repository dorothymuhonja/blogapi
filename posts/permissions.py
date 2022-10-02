from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    # Read-only permissions are allowed for any request
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permission are only allowed to the author
        return obj.author == request.user