from django.urls import path
from .import views

urlpatterns = [
    path('category/',views.CategoryList.as_view()),
    path('course/',views.CourseList.as_view()),
    path('course/<int:pk>/',views.CourseDetailView.as_view()),
    path('chapter/',views.ChapterList.as_view()),
    path('coursechapters/<int:course_id>',views.CourseChapterList.as_view()),
    path('chapter/<int:pk>',views.ChapterDetailView.as_view()),
   
]