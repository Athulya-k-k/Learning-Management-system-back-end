from rest_framework import serializers
from .models import StudentCourseEnrollment


class StudentCourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentCourseEnrollment
        fields=['id','course','student','enrolled_time']
    
    def __init__(self, *args,**kwargs):
        super(StudentCourseEnrollSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2