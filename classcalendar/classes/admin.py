from django.contrib import admin
from .models import Course, Class

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('course', 'start_time', 'end_time', 'created_at')
    search_fields = ('course__name',)
    list_filter = ('course__name', 'start_time', 'end_time', 'created_at')