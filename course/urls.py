from django.urls import path
from .import views

urlpatterns = [
    path('category/',views.CategoryList.as_view()),
    path('course/',views.CourseList.as_view()),
    path('chapter/',views.ChapterList.as_view()),
]