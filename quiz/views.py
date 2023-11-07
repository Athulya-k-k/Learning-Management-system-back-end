from django.shortcuts import render
from .serializers import QuizSerializer,QuestionSerializer
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

class QuizQuestion(generics.ListAPIView):
    serializer_class=QuestionSerializer

    def get_queryset(self):
        quiz_id=self.kwargs['quiz_id']
        quiz=models.Quiz.objects.get(pk=quiz_id)
        return models.QuizQuestions.objects.filter(quiz=quiz)
