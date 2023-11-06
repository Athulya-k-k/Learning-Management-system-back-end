from django.shortcuts import render
from rest_framework import generics
from .import models
from .serializers import NotificationSerializer

# Create your views here.

class NotificationList(generics.ListCreateAPIView):
    queryset=models.Notification.objects.all()
    serializer_class=NotificationSerializer

    def get_queryset(self):
        student_id=self.kwargs['student_id']
        student=models.Student.objects.get(pk=student_id)
        return models.Notification.objects.filter(student=student,notify_for='student',notify_subject='assignment',notify_read_status=False)