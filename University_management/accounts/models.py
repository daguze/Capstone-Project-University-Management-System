
from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

# Create your models here.
class User(AbstractUser):
    Full_name = models.CharField(max_length=100)
    Entry_date = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.Username
    

class Staff_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.Full_name} is in {self.department}"


class Student_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.Full_name} is a student in {self.department}"