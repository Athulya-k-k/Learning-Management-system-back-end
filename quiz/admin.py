from django.contrib import admin
from .models import Quiz,QuizQuestions,CourseQuiz,AttemptQuiz

# Register your models here.
admin.site.register(Quiz)
admin.site.register(QuizQuestions)
admin.site.register(CourseQuiz)
admin.site.register(AttemptQuiz)