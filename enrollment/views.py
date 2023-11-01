from django.shortcuts import render
from rest_framework import generics
from student.models import Student
from .import models
from .serializers import StudentCourseEnrollSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from course.models import Course 





@csrf_exempt
def fetch_enroll_status(request, student_id, course_id):
    try:
        student = Student.objects.get(pk=student_id)
        course = Course.objects.get(pk=course_id)
        
        # Check if the enrollment already exists
        enrollment, created = models.StudentCourseEnrollment.objects.get_or_create(student=student, course=course)
        
        if created:
            return JsonResponse({'message': 'Enrollment successful.'})
        else:
            return JsonResponse({'message': 'Student is already enrolled in this course.'})
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found.'})
    except Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found.'})

class EnrolledstudentList(generics.ListAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer

    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=Course.objects.get(pk=course_id)
        return models.StudentCourseEnrollment.objects.filter(course=course)
    

class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer
   


class Meta:     
        abstract = True