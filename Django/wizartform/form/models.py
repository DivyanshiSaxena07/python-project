from django.db import models


class Accountholders(models.Model):
        firstName=models.CharField(max_length = 120)
        lastname=models.CharField(max_length = 120)
        email = models.CharField(max_length=20)
        number=models.CharField(max_length = 12)
        gender=models.CharField(max_length = 120)
        fathername = models.CharField(max_length = 120)
        smdId = models.TextField(max_length = 120)
        pan = models.TextField(max_length = 120)
        date=models.DateField()
        adhar = models.CharField(max_length = 120)
        nName = models.CharField(max_length = 120)
        age = models.IntegerField()
        relation = models.CharField(max_length = 120)
        accNo=models.IntegerField()
        ifsc = models.TextField(max_length = 120)
        hno = models.IntegerField()
        address = models.CharField(max_length = 120)
        browser = models.CharField(max_length = 120)
        city = models.CharField(max_length = 120)
        landmark = models.CharField(max_length = 120)
        
        def __str__(self):
         return self.firstName
    
# Create your models here.
