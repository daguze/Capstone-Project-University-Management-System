
from django.urls import path
from .views import (home, login_user, logout_user, StudentListView, who_is_logged, StaffListView, StudentProfileView, StudentDetailView, StaffDetailView,
students_list_view, student_detail_view,students_list_view, student_detail_view, student_edit_view)


urlpatterns = [
    path('',home, name='home'),
    path('home/',home, name='home'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('students/', students_list_view, name='students-list-page'),
    path('students/<int:user_id>/', student_detail_view, name='student-detail-page'),
    path('students/<int:user_id>/edit/', student_edit_view, name='student-edit-page'),
    path('api/whoami/', who_is_logged, name='whoami'),
    path('api/students/', StudentListView.as_view(), name='students-list'),
    path('api/staff/', StaffListView.as_view(), name='staff-list'),
    path('api/me/student/', StudentProfileView.as_view(), name='my-student-profile'),
    path("api/students/<int:user_id>/", StudentDetailView.as_view(), name="student-detail"),
    path("api/staff/<int:user_id>/", StaffDetailView.as_view(), name="Staff-detail"),
    path("students/", students_list_view, name="students-list-page"),
    path("students/<int:user_id>/", student_detail_view, name="student-detail-page"),

    
]


    