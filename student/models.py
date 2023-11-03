from django.db import models


class Student(models.Model):
    fullname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    password=models.CharField( max_length=50)
    username=models.CharField( max_length=50)
    interest=models.TextField()
    
    def __str__(self) :
        return self.fullname


    
