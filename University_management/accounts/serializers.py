from rest_framework import serializers
from .models import Staff_user, Student_user, User
from Courses.models import Grade

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


#the one i imported from course app

class gradeserializer(serializers.ModelSerializer):
    course_code = serializers.CharField(source="course.code")
    course_title = serializers.CharField(source="course.title")
    class Meta:
        model = Grade
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    grades = serializers.SerializerMethodField()

    class Meta:
        model = Student_user
        fields = ["id", "department", "date_joined", "user", "grades"]