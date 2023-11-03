from django.db import models

class CourseRating(models.Model):
     student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='enrolled_student_rating', null=True, default=None)
     review_time = models.DateTimeField(auto_now_add=True)
     course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='enrolled_courses_rating', null=True, default=None)
     rating=models.PositiveBigIntegerField(default=0)
     reviews=models.TextField(null=True)

     def __str__(self):
         return f"{self.course}-{self.student}-{self.rating}"
