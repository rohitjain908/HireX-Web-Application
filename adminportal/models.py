from django.db import models

# Create your models here.

class Recruiter(models.Model):
  username=models.CharField(max_length=20)
  password=models.CharField(max_length=15)

class Add_Question(models.Model):
  Question=models.TextField()
  Option_A=models.TextField()
  Option_B=models.TextField()
  Option_C=models.TextField()
  Option_D=models.TextField()
  Correct_Answer=models.TextField()
  Tag=models.TextField()
