
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPES =(
        ('admin', 'Admin'), 
        ('staff', 'Staff'), 
        ('student', 'Student'),
    ) 
    user_type = models.CharField(max_length=50, choices=USER_TYPES)
    full_name = models.CharField(max_length=100, null=True)
    registration_Date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.username
    

class Staff_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.full_name} is in {self.department}"


class Student_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True,)
    

    def __str__(self):
        return f"{self.user.full_name} is a student in {self.department}"