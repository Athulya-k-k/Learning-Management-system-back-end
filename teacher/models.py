from django.db import models

class Teacher(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    skills=models.TextField()

    def __str__(self) :
        return self.fullname