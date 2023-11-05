from django.db import models
from course.models import Course
from teacher.models import Teacher


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
    


class StudentAssignment(models.Model):
     teacher= models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, default=None)
     student = models.ForeignKey('student.Student', on_delete=models.CASCADE, null=True, default=None)
     title = models.CharField(max_length=250)
     detail=models.TextField(null=True)
     add_time=models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"{self.title}"
