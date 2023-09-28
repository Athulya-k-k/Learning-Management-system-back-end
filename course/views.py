from django.shortcuts import render
from .models import CourseCategory
from .import models
from rest_framework import generics
from .serializers import CategorySerializer
from .serializers import CourseSerializer,ChapterSerializer
from .models import Course,Chapter


class CategoryList(generics.ListCreateAPIView):
    queryset=models.CourseCategory.objects.all()
    serializer_class=CategorySerializer

class CourseList(generics.ListCreateAPIView):
    queryset=models.Course.objects.all()
    serializer_class=CourseSerializer
  

class ChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer
  
