from rest_framework import serializers
from rest_framework.fields import empty
from .models import Quiz,QuizQuestions,CourseQuiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=['id','teacher','title','detail','add_time','assign_status']
        
    def __init__(self, *args,**kwargs):
        super(QuizSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=QuizQuestions
        fields=['id','quiz','questions','ans1','ans2','ans3','ans4','right_ans']

    def __init__(self, *args,**kwargs):
        super(QuestionSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1


class CourseQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseQuiz
        fields=['id','teacher','course','quiz','add_time']
    
    def __init__(self, *args,**kwargs):
        super(CourseQuizSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2