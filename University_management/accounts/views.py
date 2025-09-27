from rest_framework import permissions, generics
from rest_framework.response import Response
from.models import Staff_user, Student_user, User
from .serializers import StaffUserSerializer, StudentUserSerializer
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .permissions import IsAdmin, IsStaff, IsStaffOrAdmin,IsStudent
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
def home(request):
    return render(request, 'accounts/home.html')




def login_user(request):

    student_record_data = Student_user.objects.all()
    staff_record_data = Staff_user.objects.all()
    user_record_data = User.objects.all()
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
                return redirect('login')
            elif user.user_type == 'student':
                messages.success(request, f"Hello student {Username}")
                return redirect('login')
            else:
                messages.error(request, "Unknown user type.")
                return redirect('login')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    context = {
        'students': student_record_data,
        'staffs': staff_record_data,
        'users': user_record_data
    }
    return render(request, 'accounts/login.html', context)
  

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
  


class StudentListView(generics.ListAPIView):
    queryset = Student_user.objects.select_related("user").all()
    serializer_class = StudentUserSerializer
    permission_classes = [IsStaffOrAdmin]


class StaffListView(generics.ListAPIView):
    queryset = Staff_user.objects.select_related("user").all()
    serializer_class = StaffUserSerializer
    permission_classes = [IsStaffOrAdmin]

class StudetProfileView(generics.ListAPIView):
    serializer_class = StudentUserSerializer
    permission_classes = [IsStaffOrAdmin]