from rest_framework import serializers
from .models import Course, Class

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description']

class ClassSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Class
        fields = ['course', 'start_time', 'end_time']

