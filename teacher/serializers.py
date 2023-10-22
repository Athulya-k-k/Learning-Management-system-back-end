from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','fullname','detail','email','password','qualification','mobile_no','skills','teacher_courses','skill_list']
        depth=1