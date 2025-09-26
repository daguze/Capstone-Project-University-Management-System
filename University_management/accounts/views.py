from rest_framework import permissions, generics
from rest_framework.response import Response
from.models import Staff_user, Student_user
from .serializers import StaffUserSerializer, StudentUserSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'accounts/home.html')

from .models import Staff_user, Student_user, User


def login_user(request):

    record_data = Student_user.objects.all()
    if request.method == 'POST':
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request, username=Username, password=Password)
        if user is not None:
            login(request, user)
            # Check user type and redirect accordingly
            if user.user_type == 'admin':
                messages.success(request, f"Hello Admin {Username}")
                return redirect('login')
            elif user.user_type == 'staff':
                messages.success(request, f"Hello staff member {Username}")
                return redirect('home')
            elif user.user_type == 'student':
                messages.success(request, f"Hello student {Username}")
                return redirect('home')
            else:
                messages.error(request, "Unknown user type.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'accounts/login.html', {'records':record_data})
  

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
  