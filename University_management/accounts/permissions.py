from rest_framework import permissions




class IsAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'admin' and request.user.is_authenticated

class IsStaff(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'staff' and request.user.is_authenticated

class IsStudent(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'student' and request.user.is_authenticated

class IsStaffOrAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type in ['admin', 'staff'] and request.user.is_authenticated
