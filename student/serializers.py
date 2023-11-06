from rest_framework import serializers
from .models import Student,StudentFavoriteCourse,StudentAssignment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','fullname','email','username','password','interest',]



class StudentFavoriteCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentFavoriteCourse
        fields=['id','course','student','status']
    
    def __init__(self, *args,**kwargs):
        super(StudentFavoriteCourseSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2


class StudentAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentAssignment
        fields=['id','teacher','student','title','detail','student_status','add_time']
        
    def __init__(self, *args,**kwargs):
        super(StudentAssignmentSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2