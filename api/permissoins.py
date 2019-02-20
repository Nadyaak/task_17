from rest_framework.permissions import  BasePermission



class IsOwner(BasePermission):
    def has_object_permission(self, requast,view,obj):
        if requast.user.is_staff or (obj.owner == requast.user):
            return True
        return False
