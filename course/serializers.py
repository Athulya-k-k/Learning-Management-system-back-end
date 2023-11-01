from rest_framework import serializers
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
        depth=1

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields=['id','course','title','description','video','remarks']