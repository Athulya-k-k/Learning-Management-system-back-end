from django.urls import path
from .import views

urlpatterns = [
    path('study-materials/<int:course_id>',views.StudyMaterialList.as_view()),
  path('study-materials/<int:pk>/', views.StudyMaterialDetailView.as_view(), name='study-material-detail'),
    path('user/study-materials/<int:course_id>',views.StudyMaterialList.as_view()),

  
   
   
]