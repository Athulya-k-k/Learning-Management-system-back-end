from django.shortcuts import render
from rest_framework import generics
from student.models import Student
from .import models
from .serializers import StudentCourseEnrollSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from course.models import Course
from .models  import StudentCourseEnrollment
from teacher.models import Teacher

def fetch_enroll_status(request, student_id, course_id):
        student = Student.objects.filter(id=student_id).first()
        course = Course.objects.filter(id=course_id).first()
        enrollStatus=StudentCourseEnrollment.objects.filter(course=course,student=student).count()
        if enrollStatus:
              return JsonResponse({'bool':True})
        else:
              return JsonResponse({'bool':False})


class EnrolledstudentList(generics.ListAPIView):
    queryset=models.StudentCourseEnrollment.objects.all()
    serializer_class=StudentCourseEnrollSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id=self.kwargs['course_id']
            course=Course.objects.get(pk=course_id)
            return models.StudentCourseEnrollment.objects.filter(course=course)
        
        elif 'teacher_id' in self.kwargs:
            teacher_id=self.kwargs['teacher_id']
            teacher=Teacher.objects.get(pk=teacher_id)
            return models.StudentCourseEnrollment.objects.filter(course__teacher=teacher).distinct()
              
    

class StudentEnrollCourseList(generics.ListCreateAPIView):
    queryset = models.StudentCourseEnrollment.objects.all()
    serializer_class = StudentCourseEnrollSerializer
   


class Meta:     
        abstract = True



 