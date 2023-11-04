from django.urls import path
from .import views

urlpatterns = [
    path('student-enroll-course/',views.StudentEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>',views.fetch_enroll_status),
    path('fetch-enrolled-students/<int:course_id>/', views.EnrolledstudentList.as_view()),
    path('fetch-enrolled-courses/<int:student_id>/', views.EnrolledstudentList.as_view()),
   
    path('fetch-all-enrolled-students/<int:teacher_id>/', views.EnrolledstudentList.as_view()),

   
]