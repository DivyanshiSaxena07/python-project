from django.db import models

class Contact(models.Model):
      name=models.CharField(max_length = 120)
      email=models.CharField(max_length = 120)
      phone=models.CharField(max_length = 12)
      msg=models.TextField(max_length = 120)
      subject=models.CharField(max_length = 120)
      date=models.DateField()
# Create your models here.

      def __str__(self):
       return self.name


class Customer(models.Model):
      name=models.CharField(max_length=120)
      email=models.CharField(max_length=120)
      phone=models.CharField(max_length=12)
      address=models.TextField()
      
      def __str__(self):
       return self.name
