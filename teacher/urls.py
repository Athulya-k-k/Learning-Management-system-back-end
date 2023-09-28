from django.urls import path
from .import views

urlpatterns = [
    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view()),
    path('teacher-login',views.teacher_login),
    path('teachercourses/<int:teacher_id>',views.TeacherCourseList.as_view()),
]


