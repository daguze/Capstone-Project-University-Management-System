from django.shortcuts import render
from rest_framework import generics, permissions, filters
from accounts.models import Student_user,User
from .models import Course, Grade
from .serializers import CourseSerializers, GradeSerializers
from accounts.permissions import IsAdmin, IsStaff, IsStaffOrAdmin,IsStudent
# Create your views here.


#this is for the courses
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializers
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code','title', 'department', 'instructor__user__full_name']
    ordering_fields = ['code', 'title', 'id']
    ordering = ['code']

class CourseCreateView(generics.CreateAPIView):
    serializer = CourseSerializers
    queryset = Course.objects.all()
    permission_classes = [IsStaffOrAdmin]

class CourseUpdateView(generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializers
    permission_classes = [IsStaffOrAdmin]

class CourseDeleteView(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer = CourseSerializers
    permission_classes = [IsStaffOrAdmin]




#this isfor the grade

class GradeListView(generics.ListAPIView):
    def a_query(self):
        user = self.request.user
        q_s = Grade.objects.select_related('student__user', 'course__instructor__user')
        if User.user_type=='staff' or User.user_type=='admin':
            return Grade.objects.all()
        else:
            return q_s.filter(Student_user.objects.filter(user=user))


class GradeDetailView(generics.RetrieveAPIView):
    queryset = Grade.objects.select_related('student__user', 'course').all()
    serializer_class = GradeSerializers
    permission_classes = [permissions.IsAuthenticated, IsStudent,IsStaff]


class GradeCreateView(generics.CreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializers
    permission_classes = [permissions.IsAuthenticated, IsStaffOrAdmin]


class GradeUpdateView(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializers
    permission_classes = [permissions.IsAuthenticated, IsStaffOrAdmin]


class GradeDeleteView(generics.DestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializers
    permission_classes = [permissions.IsAuthenticated, IsStaffOrAdmin]