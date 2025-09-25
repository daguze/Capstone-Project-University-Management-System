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
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_check = authenticate(request, username=username, password=password)
        if user_check is not None:
            login(request, user_check)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout_user(request):
    messages.success(request, "You have been logged out.")
    return redirect('home')
  