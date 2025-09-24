from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login(template_name="registration/login.html"), name='login'),
    path('logout/', views.user_logout, name='logout'),
]