from rest_framework import permissions




class IsAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'admin'

class IsStaff(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'staff'

class IsStudent(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type == 'student'

class IsStaffOrAdmin(permissions.BasePermission):
    
    def has_permission(self, request, view):
        return request.user.user_type in ['admin', 'staff']
