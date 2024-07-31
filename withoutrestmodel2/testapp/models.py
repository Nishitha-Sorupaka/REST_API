from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=64)
    rollno = models.CharField(max_length=64)
    marks = models.IntegerField()
    gf = models.CharField(max_length=64)
    bf = models.CharField(max_length=64)