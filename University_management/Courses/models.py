from django.db import models
from accounts.models import Student_user, Staff_user
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100, blank=True)
    instructor = models.ForeignKey(Staff_user, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.title}"
    

class Grade(models.Model):
    student = models.ForeignKey(Student_user, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student.user.full_name} - {self.course.code}: {self.score}"
