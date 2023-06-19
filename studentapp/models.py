from django.db import models
 # Create your models here.
 # creating models here and storing in database acts as mysql

class Student(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    faculty = models.CharField(max_length=50,default=" ")
    semester = models.CharField(max_length=50,default=" ")
    phone = models.CharField(max_length=50,default=" ")
    email = models.EmailField(max_length=50,default=" ")