from rest_framework import permissions, generics
from rest_framework.response import Response
from.models import Staff_user, Student_user
from .serializers import StaffUserSerializer, StudentUserSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'accounts/home.html')

def login_user(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user_check = authenticate(request, username=Username, password=Password)
        if user_check is not None:
            login(request, user_check)
            if getattr(user_check, 'user_type', None) == 'staff':
                messages.success(request, "You have successfully logged in.")
                
            elif getattr(user_check, 'user_type', None) == 'student':
                messages.success(request, "You have successfully logged in.")
                
            else:
                messages.success(request, "You have successfully logged in.")        
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
  

