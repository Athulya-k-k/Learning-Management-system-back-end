from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeacherSerializer
from .models import Teacher
from .import models
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from course.serializers import CourseSerializer
from course.models import Course


class TeacherList(generics.ListCreateAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Teacher.objects.all()
    serializer_class=TeacherSerializer
    # permission_classes=[permissions.IsAuthenticated]
   
@csrf_exempt
def teacher_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            teacherData = models.Teacher.objects.get(email=email, password=password)
        except models.Teacher.DoesNotExist:
            teacherData=None
        if teacherData:
                return JsonResponse({'bool': True,'teacher_id':teacherData.id})
        else:
                return JsonResponse({'bool': False})
     
         


#specific teacher course

class TeacherCourseList(generics.ListCreateAPIView):
    serializer_class=CourseSerializer


    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=models.Teacher.objects.get(pk=teacher_id)
        return Course.objects.filter(teacher=teacher)




class TeacherCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Course.objects.all()
    serializer_class=CourseSerializer
   




@csrf_exempt
def teacher_change_password(request,teacher_id):
        password = request.POST.get('password')
        try:
            teacherData =models.Teacher.objects.get(id=teacher_id)
        except models.Teacher.DoesNotExist:
            teacherData=None
        if teacherData:
                models.Teacher.objects.filter(id=teacher_id).update(password=password)
                return JsonResponse({'bool': True,})
        else:
                return JsonResponse({'bool': False})
     


        
