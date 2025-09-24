from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Staff_user, Student_user, Admin_user
from rest_framework import viewsets
from .serializer import UserSerializer, StaffUserSerializer, StudentUserSerializer, AdminUserSerializer

# Create your views here.


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class home(generic.TemplateView):
    template_name = 'accounts/home.html'
    def get(self, request):
        return HttpResponse("Welcome to the University Management System")
    



class Staff_userViewSet(viewsets.ModelViewSet):
    queryset = Staff_user.objects.all()
    serializer_class = StaffUserSerializer
class Student_userViewSet(viewsets.ModelViewSet):
    queryset = Student_user.objects.all()
    serializer_class = StudentUserSerializer

class Admin_userViewSet(viewsets.ModelViewSet):
    queryset = Admin_user.objects.all()
    serializer_class = AdminUserSerializer