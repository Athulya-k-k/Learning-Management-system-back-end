from django.urls import path
from .import views

urlpatterns = [
    path('quiz/',views.QuizList.as_view()),
    path('teacher-quiz/<int:teacher_id>',views.TeacherQuizList.as_view()),
  
   

   
]