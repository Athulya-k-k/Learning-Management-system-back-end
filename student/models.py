from django.db import models
from course.models import Course

class Student(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    username=models.CharField( max_length=50)
    interest=models.TextField()
    
    def __str__(self) :
        return self.fullname

class StudentCourseEnrollment(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrolled_courses')
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='enrolled_student')
    enrolled_time=models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"{self.course}-{self.student}"

    
