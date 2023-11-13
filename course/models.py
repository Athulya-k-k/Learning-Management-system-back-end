from django.db import models
from teacher.models import Teacher
from django.core import serializers
from enrollment.models import StudentCourseEnrollment
from rating.models import CourseRating


class CourseCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name_plural="Course Categories"


    def __str__(self):
        return self.title

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name='courses')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE,related_name='teacher_courses')
    title = models.CharField(max_length=100)
    description = models.TextField()
    featured_img=models.ImageField(upload_to='course_imgs/',null=True)
    techs = models.TextField(null=True)

    def __str__(self):
        return self.title
    
    def related_videos(self):
        reated_videos=Course.objects.filter(techs__icontains=self.techs)
        return serializers.serialize('json',reated_videos)
    
    def tech_list(self):
        tech_list=self.techs.split(',')
        return tech_list
    
    def total_enrolled_students(self):
        total_enrolled_students=StudentCourseEnrollment.objects.filter(course=self).count()
        return total_enrolled_students
    
    # def course_rating(self):
    #    course_rating=CourseRating.objects.filter(course=self).aaggregate(avg_rating=models.Avg('rating'))
    #    return course_rating
    
    
    
    

    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course_chapters')
    title = models.CharField(max_length=100)
    description = models.TextField()
    video=models.FileField(upload_to='chapter_videos/',null=True)
    remarks= models.TextField(null=True)




   


    