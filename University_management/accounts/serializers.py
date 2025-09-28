from rest_framework import serializers
from .models import Staff_user, Student_user, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class StaffUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff_user
        fields = '__all__'

class StudentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_user
        fields = '__all__'
