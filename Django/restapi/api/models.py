from django.db import models

class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=40)
    age=models.IntegerField()

# Create your models here.
