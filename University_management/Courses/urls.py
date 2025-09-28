from django.urls import path
from .views import (
    CourseListView, CourseCreateView, CourseUpdateView, CourseDeleteView,
    GradeListView, GradeCreateView, GradeUpdateView,
    GradeDeleteView, GradeDetailView
)
app_name = 'Courses'
urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/create/', CourseCreateView.as_view(), name='course-create'),
    path('courses/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('grades/', GradeListView.as_view(), name='grade-list'),
    path('grades/create/', GradeCreateView.as_view(), name='grade-create'),
    path('grades/<int:pk>/', GradeDetailView.as_view(), name='grade-detail'),
    path('grades/<int:pk>/update/', GradeUpdateView.as_view(), name='grade-update'),
    path('grades/<int:pk>/delete/', GradeDeleteView.as_view(), name='grade-delete'),
]