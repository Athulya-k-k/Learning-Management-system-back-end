from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.StudentList.as_view()),
    path('student-login',views.student_login),
    path('student-add-favorite-course/',views.StudentFavoriteCourseList.as_view()),
    path('student-remove-favorite-course/<int:course_id>/<int:student_id>',views.remove_favourite_course),
    path('fetch-favorite-status/<int:student_id>/<int:course_id>',views.fetch_favourite_status),
    path('fetch-favorite-courses/<int:student_id>',views.StudentFavoriteCourseList.as_view()),
    path('student-assignment/<int:teacher_id>/<int:student_id>',views.AssignmentList.as_view()),
    path('my-assignments/<int:student_id>',views.MyAssignmentList.as_view()),
    path('update-assignment/<int:pk>',views.UpdateAssignment.as_view()),
    path('student/dashboard/<int:pk>/',views.StudentDashboard.as_view()),
    path('student/<int:pk>/',views.StudentDetail.as_view()),
    path('student/change-password/<int:student_id>/',views.student_change_password),
  
]