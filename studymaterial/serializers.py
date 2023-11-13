from rest_framework import serializers
from rest_framework.fields import empty
from .models import StudyMaterial



class StudyMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudyMaterial
        fields=['id','course','title','description','upload','remarks']

    def __init__(self, *args,**kwargs):
        super(StudyMaterialSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=1
