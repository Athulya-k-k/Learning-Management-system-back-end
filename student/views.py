from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .import models
from .serializers import StudentSerializer,StudentFavoriteCourseSerializer,StudentAssignmentSerializer,StudentDashboardSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from course.models import Course
from rest_framework.response import Response
from teacher.models import Teacher


class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer
    # permission_classes=[permissions.IsAuthenticated]

   
@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            studentData = models.Student.objects.get(email=email, password=password)
        except models.Student.DoesNotExist:
            studentData=None
        if studentData:
                return JsonResponse({'bool': True,'student_id':studentData.id})
        else:
                return JsonResponse({'bool': False})
     



class StudentFavoriteCourseList(generics.ListCreateAPIView):
     queryset=models.StudentFavoriteCourse.objects.all()
     serializer_class=StudentFavoriteCourseSerializer

     def get_queryset(self):
       if 'student_id' in self.kwargs:
            student_id=self.kwargs['student_id']
            student=Student.objects.get(pk=student_id)
            return models.StudentFavoriteCourse.objects.filter(student=student).distinct()
    
              



def fetch_favourite_status(request,student_id,course_id):
     student=models.Student.objects.filter(id=student_id).first()
     course=Course.objects.filter(id=course_id).first()
     favoriteStatus=models.StudentFavoriteCourse.objects.filter(course=course,student=student).first()
     if favoriteStatus and favoriteStatus.status == True:
          return JsonResponse({'bool':True})
     else:
          return JsonResponse({'bool':False})
     
@csrf_exempt
def remove_favourite_course(request,course_id,student_id):
     student=models.Student.objects.filter(id=student_id).first()
     course=Course.objects.filter(id=course_id).first()
     favoriteStatus=models.StudentFavoriteCourse.objects.filter(course=course,student=student).delete()
     if favoriteStatus :
          return JsonResponse({'bool':True})
     else:
          return JsonResponse({'bool':False})

class AssignmentList(generics.ListCreateAPIView):
    queryset=models.StudentAssignment.objects.all()
    serializer_class=StudentAssignmentSerializer

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        teacher_id=self.kwargs['teacher_id']
        student=models.Student.objects.get(pk=student_id)
        teacher=Teacher.objects.get(pk=teacher_id)
        return models.StudentAssignment.objects.filter(student=student,teacher=teacher)



class MyAssignmentList(generics.ListCreateAPIView):
    queryset=models.StudentAssignment.objects.all()
    serializer_class=StudentAssignmentSerializer

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=models.Student.objects.get(pk=student_id)
        return models.StudentAssignment.objects.filter(student=student)



class UpdateAssignment(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudentAssignment.objects.all()
    serializer_class = StudentAssignmentSerializer



class StudentDashboard(generics.RetrieveAPIView):
     queryset=models.Student.objects.all()
     serializer_class=StudentDashboardSerializer





    