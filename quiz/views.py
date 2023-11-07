from django.shortcuts import render
from .serializers import QuizSerializer
from rest_framework import generics
from .models import Quiz
from .import models
from teacher.models import Teacher
# Create your views here.



class QuizList(generics.ListCreateAPIView):
    queryset=models.Quiz.objects.all()
    serializer_class=QuizSerializer


class TeacherQuizList(generics.ListCreateAPIView):
    serializer_class=QuizSerializer


    def get_queryset(self):
        teacher_id=self.kwargs['teacher_id']
        teacher=Teacher.objects.get(pk=teacher_id)
        return models.Quiz.objects.filter(teacher=teacher)
    

class TeacherQuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= models.Quiz.objects.all()
    serializer_class=QuizSerializer
   

 
class QuizDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Quiz.objects.all()
    serializer_class=QuizSerializer
