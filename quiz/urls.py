from django.urls import path
from .import views

urlpatterns = [
    path('quiz/',views.QuizList.as_view()),
    path('teacher-quiz/<int:teacher_id>',views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>',views.TeacherQuizDetail.as_view()),
    path('quiz/<int:pk>',views.QuizDetail.as_view()),
  
   

   
]