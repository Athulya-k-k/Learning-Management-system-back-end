from django.urls import path
from .import views

urlpatterns = [
    path('student/fetch-all-notifications/<int:student_id>/',views.NotificationList.as_view()),
    path('save-notification/',views.NotificationList.as_view()),
   

   
]