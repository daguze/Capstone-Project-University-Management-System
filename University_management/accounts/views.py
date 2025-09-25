from rest_framework import permissions, generics
from rest_framework.response import Response
from.models import Staff_user, Student_user
from .serializers import StaffUserSerializer, StudentUserSerializer
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'accounts/home.html')

def login_user(request):
    return render(request, 'accounts/login.html')

def logout_user(request):
    messages.success(request, "You have been logged out.")
    return render(request, 'accounts/login.html')
