from rest_framework import serializers
from .models import StudentCourseEnrollment


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentCourseEnrollment
        fields=['id','course','student','enrolled_time']
        depth=1