from django.db import models

class StudentCourseEnrollment(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='enrolled_student', null=True, default=None)
    enrolled_time = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='enrolled_courses', null=True, default=None)

    def __str__(self):
        return f"{self.course}-{self.student}"



