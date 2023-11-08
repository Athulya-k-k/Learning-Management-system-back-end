from django.urls import path
from .import views

urlpatterns = [
    path('quiz/',views.QuizList.as_view()),
    path('teacher-quiz/<int:teacher_id>',views.TeacherQuizList.as_view()),
    path('teacher-quiz-detail/<int:pk>',views.TeacherQuizDetail.as_view()),
    path('quiz/<int:pk>',views.QuizDetail.as_view()),
    path('quiz-questions/<int:quiz_id>',views.QuizQuestion.as_view()),
    path('quiz-assign-course/',views.CourseQuizList.as_view()),
    path('fetch-quiz-assign-status/<int:quiz_id>/<int:course_id>',views.fetch_quiz_assign_status),
   

   
]