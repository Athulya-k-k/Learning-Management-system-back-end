from rest_framework import serializers
from rest_framework.fields import empty
from .models import CourseRating



class CourseRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseRating
        fields=['id','course','student','rating','reviews','review_time']

    def __init__(self, *args,**kwargs):
        super(CourseRatingSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1