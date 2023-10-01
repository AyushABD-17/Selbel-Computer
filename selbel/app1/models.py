from django.db import models

# Create your models here.

class services(models.Model):
    title=models.CharField(max_length=60)
    desc=models.TextField(max_length=200)
    duration=models.TextField(max_length=20)
    fee=models.TextField(max_length=10)
    img=models.ImageField(upload_to='ser',blank=True,null=True)

    def __str__(self):
        return self.title
    
class team(models.Model):
    name=models.CharField(max_length=60)
    title=models.CharField(max_length=30,default='SOME STRING')
    experience=models.CharField(max_length=20)
    desc=models.TextField(max_length=100)
    img=models.ImageField(upload_to='team',blank=True,null=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name= models.CharField(max_length=25)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=10)
    subject=models.TextField(max_length=30,default="abc")
    msg=models.TextField(max_length=200,default="wer")
    
    def __str__(self):
        return self.name
    
# About Section:-
class about(models.Model):
    course_id=models.AutoField
    course_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=300)

    

    def __str__(self):
        return self.course_name_name

