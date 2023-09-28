from django.urls import path
from .import views

urlpatterns = [
    path('student/',views.TeacherList.as_view()),
]