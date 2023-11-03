from django.urls import path
from .import views

urlpatterns = [
    path('teacher/',views.TeacherList.as_view()),
    path('teacher/<int:pk>/',views.TeacherDetail.as_view()),
    path('teacher/change-password/<int:teacher_id>/',views.teacher_change_password),
    path('teacher-login',views.teacher_login),
    path('teachercourses/<int:teacher_id>',views.TeacherCourseList.as_view()),
    path('teachercourse-detail/<int:pk>',views.TeacherCourseDetail.as_view()),
]


