from django.db import models
from course.models import Course
from teacher.models import Teacher
from enrollment.models import StudentCourseEnrollment


class Student(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50,null=True,blank=True)
    username=models.CharField( max_length=50)
    interest=models.TextField()
    profile_img=models.ImageField(upload_to='student_profile_imgs/',null=True)
    
    def __str__(self) :
        return self.fullname
    

    def enrolled_courses(self):
        enrolled_courses=StudentCourseEnrollment.objects.filter(student=self).count()
        return enrolled_courses

    def favorite_courses(self):
        favorite_courses=StudentFavoriteCourse.objects.filter(student=self).count()
        return favorite_courses

    def complete_assignments(self):
        complete_assignments=StudentAssignment.objects.filter(student=self,student_status=True).count()
        return complete_assignments
    
    def pending_assignments(self):
        pending_assignments=StudentAssignment.objects.filter(student=self,student_status=False).count()
        return pending_assignments


    
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
     student_status=models.BooleanField(default=False,null=True)
     add_time=models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return f"{self.title}"
