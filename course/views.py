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

    def get_queryset(self):
        qs=super().get_queryset()
        if 'result' in self.request.GET:
            limit=int(self.request.GET['result'])
            qs=models.Course.objects.all().order_by('-id')[:limit]

        if 'category' in self.request.GET:
            category=self.request.GET['category']
            qs=models.Course.objects.filter(techs__icontains=category)


        if 'skill_name' in self.request.GET and 'teacher' in self.request.GET:
            skill_name=self.request.GET['skill_name']
            teacher=self.request.GET['teacher']
            teacher=models.Teacher.objects.filter(id=teacher).first()
            qs=models.Course.objects.filter(techs__icontains=skill_name,teacher=teacher)

        
        return qs
  

class ChapterList(generics.ListCreateAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer
  
class CourseChapterList(generics.ListAPIView):
    serializer_class=ChapterSerializer

    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=models.Course.objects.get(pk=course_id)
        return models.Chapter.objects.filter(course=course)


  
class ChapterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Chapter.objects.all()
    serializer_class=ChapterSerializer

    # def get_serializer_context(self):
    #    context=super().get_serializer_context()
    #    context['chapter_duration']=self.chapter_duration
    #    print(context)
    #    return context
  
class CourseDetailView(generics.RetrieveAPIView):
    queryset=models.Course.objects.all()
    serializer_class= CourseSerializer


