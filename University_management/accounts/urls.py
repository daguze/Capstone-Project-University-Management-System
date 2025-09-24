from django.urls import path
from .views import RegisterView, home
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name="acccounts/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home.as_view(), name='home'),
]
router = DefaultRouter()
router.register(r'staff', views.Staff_userViewSet, basename='staff')
router.register(r'students', views.Student_userViewSet, basename='students')
router.register(r'admins', views.Admin_userViewSet, basename='admins')

urlpatterns += router.urls