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
from Courses.models import Grade
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404
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
  



@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def who_is_logged(request):
    return Response({
        "id": request.user.id,
        "username": request.user.username,
    })


class StudentListView(generics.ListAPIView):
    queryset = Student_user.objects.select_related("user").all()
    serializer_class = StudentUserSerializer
    permission_classes = [IsStaffOrAdmin]


class StaffListView(generics.ListAPIView):
    queryset = Staff_user.objects.select_related("user").all()
    serializer_class = StaffUserSerializer
    permission_classes = [IsStaffOrAdmin]

class StudentProfileView(generics.ListAPIView):
    serializer_class = StudentUserSerializer
    permission_classes = [IsStaffOrAdmin]

class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student_user.objects.select_related("user").all()
    serializer_class = StudentUserSerializer
    permission_classes = [IsStaffOrAdmin]
    lookup_field = "user_id"

class StaffDetailView(generics.RetrieveAPIView):
    queryset = Staff_user.objects.select_related("user").all()
    serializer_class = StaffUserSerializer
    permission_classes = [IsStaffOrAdmin]
    lookup_field = "user_id"



def students_list_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.user_type not in ("admin", "staff"):
        messages.error(request, "unauthorised access")
        return redirect('home')

    students = (
        Student_user.objects
        .select_related("user")
        .order_by("user__full_name")
    )
    return render(request, "accounts/students_list.html", {"students": students})
def student_detail_view(request, user_id: int):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.user.user_type not in ("admin", "staff"):
        messages.error(request, "You are not authorized to view this page.")
        return redirect("home")

    student = get_object_or_404(
        Student_user.objects.select_related("user"),
        user_id=user_id,
    )

    grades = (
        Grade.objects
        .select_related("course", "student__user")
        .filter(student=student)
        .order_by("course_id")
    )


    context = {
        "student": student,
        "grades": grades,
    }
    return render(request, "accounts/student_detail.html", context)


def student_edit_view(request, user_id: int):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.user.user_type not in ("admin", "staff"):   # or == "admin" if only admin edits
        messages.error(request, "You are not authorized to edit student data.")
        return redirect("home")


    student = get_object_or_404(
        Student_user.objects.select_related("user"),
        user_id=user_id
    )
    user = student.user

    UserForm = modelform_factory(User, fields=["username", "email", "full_name", "user_type"])
    StudentForm = modelform_factory(Student_user, fields=["department"])

    if request.method == "POST":
        u_form = UserForm(request.POST, instance=User)
        s_form = StudentForm(request.POST, instance=student)
        if u_form.is_valid() and s_form.is_valid():
            u_form.save()
            s_form.save()
            messages.success(request, "Student profile updated successfully.")
            return redirect("student-detail-page", user_id=user_id)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        u_form = UserForm(instance=user)
        s_form = StudentForm(instance=student)

    return render(request, "accounts/student_edit.html", {
        "student": student,
        "u_form": u_form,
        "s_form": s_form,
    })
