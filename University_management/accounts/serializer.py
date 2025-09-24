from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Staff_user, Student_user, Admin_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_user
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined']

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_user
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'department']

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_user
        fields = ['id', 'first_name', 'last_name', 'email']