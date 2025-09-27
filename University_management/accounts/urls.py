
from django.urls import path
from .views import home, login_user, logout_user, StudentListView

urlpatterns = [
    path('',home, name='home'),
    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path("api/students/", StudentListView.as_view(), name="students-list"),
    
]


    