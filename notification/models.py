from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.
class Notification(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)

    notify_subject=models.CharField(max_length=200,null=True)
    notify_for=models.CharField(max_length=200)
    notify_created_time=models.DateTimeField(auto_now_add=True)
    notify_read_status=models.BooleanField(default=False)