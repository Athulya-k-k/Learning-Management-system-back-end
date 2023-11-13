from django.db import models
from course.models import Course

# Create your models here.
class StudyMaterial(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='course_material')
    title = models.CharField(max_length=100)
    description = models.TextField()
    upload=models.FileField(upload_to='study_materials/',null=True)
    remarks= models.TextField(null=True)
