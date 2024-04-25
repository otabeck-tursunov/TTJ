from rest_framework.permissions import BasePermission


class IsXodim(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "xodim":
            return True
        return False


class IsNazoratchi(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "nazoratchi":
            return True
        return False
