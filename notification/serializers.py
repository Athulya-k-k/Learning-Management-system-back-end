from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=['teacher','student','notify_subject','notify_for','notify_created_time','notify_read_status']
    
    def __init__(self, *args,**kwargs):
        super(NotificationSerializer,self).__init__(*args,**kwargs)
        request=self.context.get('request')
        self.Meta.depth=0
        if request and request.method =='GET':
            self.Meta.depth=2