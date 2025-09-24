from django.db import models

# Create your models here.

class Staff_user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"
    


class Student_user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)
    date_joined = models.DateField(auto_now_add=True)
    department = models.CharField(max_length=100, null=True)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email} in {self.department}"
    


class Admin_user(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=100)

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.email}"
    


