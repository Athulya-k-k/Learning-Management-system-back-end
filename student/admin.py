from django.contrib import admin
from .models import Student,StudentCourseEnrollment

admin.site.register(Student)
admin.site.register(StudentCourseEnrollment)
