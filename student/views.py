from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .import models
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse

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
     



