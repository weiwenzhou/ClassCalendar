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
        if not course_id:
            return Response({'error': 'course_id is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        now = timezone.now()
        upcoming_classes = Class.objects.filter(course=course, start_time__gte=now).order_by('start_time')

        serializer = ClassSerializer(upcoming_classes, many=True)
        return Response(serializer.data)