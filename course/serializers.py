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
        fields=['id','category','teacher','title','description','featured_img','techs']

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Chapter
        fields=['course','title','description','video','remarks']