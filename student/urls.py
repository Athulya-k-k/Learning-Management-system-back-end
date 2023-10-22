from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.StudentList.as_view()),
    path('student-login',views.student_login),
    path('student-enroll-course/',views.StudentEnrollCourseList.as_view()),
    path('fetch-enroll-status/<int:student_id>/<int:course_id>',views.fetch_enroll_status)
]