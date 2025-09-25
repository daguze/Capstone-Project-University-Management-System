from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Staff_user, Student_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']
    
class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_user
        fields = ['user', 'department']

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_user
        fields = ['user', 'department', 'date_joined']
