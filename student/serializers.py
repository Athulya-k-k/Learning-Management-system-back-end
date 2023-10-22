from rest_framework import serializers
from .models import Student,StudentCourseEnrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','fullname','email','username','password','interest',]


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentCourseEnrollment
        fields=['id','course','student','enrolled_time']
       