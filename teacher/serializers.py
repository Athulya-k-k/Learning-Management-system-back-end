from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','fullname','email','password','qualification','mobile_no','skills','profile_img','teacher_courses','skill_list']
    
    def __init__(self, *args,**kwargs):
        super(TeacherSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1


class TeacherDashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['total_teacher_courses','total_teacher_students','total_teacher_chapters']