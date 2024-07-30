from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.utils import timezone
from .models import Course, Class
from .serializers import CourseSerializer, ClassSerializer

# Create your views here.
class CourseListView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class UpcomingClassesView(APIView):
    def get(self, request):
        course_id = request.query_params.get('course_id')
        now = timezone.now()
        if course_id:
            try:
                course = Course.objects.get(id=course_id)
            except Course.DoesNotExist:
                return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

            upcoming_classes = Class.objects.filter(course=course, start_time__gte=now).order_by('start_time')
        else:
            upcoming_classes = Class.objects.filter(start_time__gte=now).order_by('start_time')

        count = request.query_params.get('count')
        if count:
            upcoming_classes = upcoming_classes[:int(count)]

        serializer = ClassSerializer(upcoming_classes, many=True)
        return Response(serializer.data)