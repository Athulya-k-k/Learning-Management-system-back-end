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


    
class StudentFavoriteCourse(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural="student fav courses"


    def __str__(self) :
        return f"{self.course}-{self.student}"