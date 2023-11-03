from django.shortcuts import render
from .import models
from rest_framework import generics
from .serializers import CourseRatingSerializer
from .models import CourseRating
from django.http import JsonResponse,HttpResponse
from student.models import Student
from course.models import Course
from .models import CourseRating

# Create your views here.
class CourseRatingList(generics.ListCreateAPIView):
   queryset=models.CourseRating.objects.all()
   serializer_class=CourseRatingSerializer




def fetch_rating_status(request, student_id, course_id):
  
        student = Student.objects.filter(id=student_id).first()
        course = Course.objects.filter(id=course_id).first()
        rating_status =models.CourseRating.objects.filter(course=course, student=student).count()
        if rating_status:
          return JsonResponse({'bool': True})
        else:
         return JsonResponse({'bool': False})
 