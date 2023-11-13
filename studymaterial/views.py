from django.shortcuts import render

from .import models
from rest_framework import generics
from .serializers import StudyMaterialSerializer
from django.http import JsonResponse,HttpResponse
from django.db.models import Q 
import logging

logger = logging.getLogger(__name__)

class StudyMaterialList(generics.ListCreateAPIView):
    serializer_class=StudyMaterialSerializer

    def get_queryset(self):
        course_id=self.kwargs['course_id']
        course=models.Course.objects.get(pk=course_id)
        return models.StudyMaterial.objects.filter(course=course)
    
class StudyMaterialDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer

    def delete(self, request, *args, **kwargs):
        logger.info("Delete method called")
        return super().delete(request, *args, **kwargs)
