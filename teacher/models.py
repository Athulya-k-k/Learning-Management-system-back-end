from django.db import models

class Teacher(models.Model):
    fullname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100,blank=True,null=True)
    qualification=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='teacher_profile_imgs/',null=True)
    skills=models.TextField()

    def __str__(self) :
        return self.fullname
    
    def skill_list(self):
        skill_list=self.skills.split(',')
        return skill_list
