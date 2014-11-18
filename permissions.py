from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
  """
  Custom permission to only allow owners of an object to edit it
  """
  def has_object_permission(self, request, view, obj):
    # Read permissions to any request
    # so we'll always allow GET, HEAD, or OPTIONS
    if request.method in permissions.SAFE_METHODS:
      return True

    # Write permissions to owners only
    return obj.owner == request.user