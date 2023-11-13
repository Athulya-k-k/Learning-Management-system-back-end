from django.shortcuts import render
from .serializers import QuizSerializer,QuizQuestionsSerializer,CourseQuizSerializer,AttemptQuizSerializer
from rest_framework import generics
from .models import Quiz,QuizQuestions
from .import models
from teacher.models import Teacher
from course.models import Course
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from student.models import Student
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

class QuizQuestion(generics.ListCreateAPIView):
    serializer_class = QuizQuestionsSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz=models.Quiz.objects.get(pk=quiz_id)
       

        if 'limit' in self.kwargs:
            return models.QuizQuestions.objects.filter(quiz=quiz).order_by('id')[:1]
        elif 'question_id' in self.kwargs:
            current_question=self.kwargs['question_id']
            return models.QuizQuestions.objects.filter(quiz=quiz,id__gt=current_question).order_by('id')[:1]
        else:
            return models.QuizQuestions.objects.filter(quiz=quiz)

class CourseQuizList(generics.ListCreateAPIView):
    queryset = models.CourseQuiz.objects.all()
    serializer_class = CourseQuizSerializer

    def get_queryset(self):
        if 'course_id' in self.kwargs:
            course_id=self.kwargs['course_id']
            course=Course.objects.get(pk=course_id)
            return models.CourseQuiz.objects.filter(course=course)

def fetch_quiz_assign_status(request,quiz_id,course_id):
    quiz=models.Quiz.objects.filter(id=quiz_id).first()
    course=Course.objects.filter(id=course_id).first()
    assignStatus=models.CourseQuiz.objects.filter(course=course,quiz=quiz).count()
    if assignStatus:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})


class AttemptQuizList(generics.ListCreateAPIView):
    queryset = models.AttemptQuiz.objects.all()
    serializer_class = AttemptQuizSerializer

def fetch_quiz_attempt_status(request,quiz_id,student_id):
    quiz=models.Quiz.objects.filter(id=quiz_id).first()
    student=Student.objects.filter(id=student_id).first()
    attemptStatus=models.AttemptQuiz.objects.filter(student=student,question__quiz=quiz).count()
    if attemptStatus>0:
        return JsonResponse({'bool':True})
    else:
        return JsonResponse({'bool':False})