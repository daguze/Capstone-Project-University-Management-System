from django.contrib import admin
from .models import Course, Grade
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "department")
    search_fields = ("code", "title", "department", "instructor__user__full_name")
    


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("course", "score")
    search_fields = ("student__user__full_name", "course__code", "course__title")
    list_select_related = ("student__user", "course")
