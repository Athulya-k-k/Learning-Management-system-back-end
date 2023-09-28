from django.db import models
from django.db import models
from teacher.models import Teacher

class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name_plural="Course Categories"


    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/',null=True)
    techs = models.TextField(null=True)

    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    video=models.FileField(upload_to='chapter_videos/',null=True)
    remarks= models.TextField(null=True)
