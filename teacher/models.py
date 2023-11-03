from django.db import models


class Teacher(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True,null=True)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='teacher_profile_imgs/',null=True)
    skills=models.TextField()

    def __str__(self) :
        return self.fullname
    
    def skill_list(self):
        skill_list=self.skills.split(',')
        return skill_list
 

    def total_teacher_courses(self):
        from course.models import Course
        total_courses=Course.objects.filter(teacher=self).count()
        return total_courses

    def total_teacher_chapters(self):
        from course.models import Chapter
        total_chapters=Chapter.objects.filter(course__teacher=self).count()
        return total_chapters

    def total_teacher_students(self):
        from enrollment.models import StudentCourseEnrollment
        total_students=StudentCourseEnrollment.objects.filter(course__teacher=self).count()
        return total_students