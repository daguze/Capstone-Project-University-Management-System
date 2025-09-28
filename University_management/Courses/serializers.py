from rest_framework import serializers
from .models import Course, Grade


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_instructor_name(self, obj):
        if obj.instructor and obj.instructor.user:
            return obj.instructor.user.full_name
        return None



class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"

    def get_student_name(self, obj):
        return obj.student.user.full_name if obj.student and obj.student.user else None