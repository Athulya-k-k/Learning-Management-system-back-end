from django.contrib import admin
from .models import Student,StudentFavoriteCourse,StudentAssignment

admin.site.register(Student)
admin.site.register(StudentFavoriteCourse)
admin.site.register(StudentAssignment)

