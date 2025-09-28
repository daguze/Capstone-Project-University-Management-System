from rest_framework import serializers
from .models import courses, grade


class coursesuserserializers(serializers.modelserializer):
    class Meta:
        model = courses
        fields = '__all__'
    
    def get_instructor_name(self, obj):
        if obj.instructor and obj.instructor.user:
            return obj.instructor.user.full_name
        return None



class gradeuserserializer(serializers.modelserializer):
    class Meta:
        model = grade
        fields = "__all__"

    def get_student_name(self, obj):
        return obj.student.user.full_name if obj.student and obj.student.user else None