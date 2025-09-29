
from django.urls import path
from .views import home, login_user, logout_user, StudentListView, who_is_logged, StaffListView, StudentProfileView, StudentDetailView, StaffDetailView

urlpatterns = [
    path('',home, name='home'),
    path('home/',home, name='home'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('api/whoami/', who_is_logged, name='whoami'),
    path('api/students/', StudentListView.as_view(), name='students-list'),
    path('api/staff/', StaffListView.as_view(), name='staff-list'),
    path('api/me/student/', StudentProfileView.as_view(), name='my-student-profile'),
    path("api/students/<int:user_id>/", StudentDetailView.as_view(), name="student-detail"),
    path("api/staff/<int:user_id>/", StaffDetailView.as_view(), name="Staff-detail"),

    
]


    