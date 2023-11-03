from rest_framework import serializers
from rest_framework.fields import empty
from .models import CourseCategory
from .models import Course,Chapter

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields=['id','title','description']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id','category','teacher','title','description','featured_img','techs','course_chapters','related_videos','tech_list','total_enrolled_students']
        
    def __init__(self, *args,**kwargs):
        super(CourseSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields=['id','course','title','description','video','remarks']

    def __init__(self, *args,**kwargs):
        super(ChapterSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1


