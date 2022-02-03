from email import message
from statistics import mode
import string
from django.db import models

# Create your models here.
class bodypartdb(models.Model):
    name = models.CharField(max_length = 30)
    part = models.CharField(max_length = 30,null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class DataSet(models.Model):
    bodypartname = models.CharField(max_length = 30)
    bodypart = models.IntegerField()
    symptom1 = models.IntegerField()
    symptom2 = models.IntegerField()
    symptom3 = models.IntegerField()
    symptom4 = models.IntegerField()
    symptom5 = models.IntegerField()
    def __str__(self):
        return self.bodypartname

class contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    subject = models.CharField(max_length = 80)
    message = models.CharField(max_length = 100)
    