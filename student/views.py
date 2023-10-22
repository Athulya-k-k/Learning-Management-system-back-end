from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .import models
from .serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset=models.Student.objects.all()
    serializer_class=StudentSerializer
    # permission_classes=[permissions.IsAuthenticated]
