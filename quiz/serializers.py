from rest_framework import serializers
from rest_framework.fields import empty
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id','teacher','title','detail','add_time']
        
    def __init__(self, *args,**kwargs):
        super(QuizSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2