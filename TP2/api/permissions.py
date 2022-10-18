from rest_framework.permissions import BasePermission
 
# Si on est admin
class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

# Si on est l'auteur du post
class IsAuthorAuthenticated(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user