import os
import django
import random
from datetime import datetime, timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'classcalendar.settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from classes.models import Course, Class

def create_superuser(username, email, password):
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser '{username}' created successfully.")
    else:
        print(f"Superuser '{username}' already exists.")

def create_courses_and_classes():
    course_names = [
        "Mathematics 101",
        "History of Art",
        "Biology Basics",
        "Introduction to Physics",
        "Computer Science Fundamentals"
    ]
    
    start_date = datetime(2024, 8, 1)
    
    courses = []
    
    # Create Courses
    for name in course_names:
        course = Course(name=name, description=f"This is the {name} course.")
        course.save()
        courses.append(course)
    
    # Create Classes for each Course
    for course in courses:
        start_hour = random.randint(8, 16)
        for i in range(0, 30, random.randint(2, 6)):
            start_time = timezone.make_aware(start_date + timedelta(days=i, hours=start_hour), timezone.get_current_timezone())
            end_time = start_time + timedelta(hours=1) # Assuming each class is 1 hour long
            class_instance = Class(course=course, start_time=start_time, end_time=end_time)
            class_instance.save()

if __name__ == "__main__":
    create_superuser('admin', 'admin@example.com', 'admin')
    create_courses_and_classes()
