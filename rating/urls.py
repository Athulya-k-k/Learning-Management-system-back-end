from django.urls import path
from .import views

urlpatterns = [

    path('course-rating/',views.CourseRatingList.as_view()),
    path('fetch-rating-status/<int:student_id>/<int:course_id>',views.fetch_rating_status),
   
]