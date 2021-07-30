from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class UserData(models.Model):
  user_id=models.ForeignKey(User, on_delete=CASCADE,default=1)
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20)
  email=models.EmailField()
  stream=models.CharField(max_length=20)
  graduation_year=models.IntegerField()
  dob=models.DateField()
  

class Resume(models.Model):
  user_id=models.ForeignKey(User, on_delete=CASCADE,default=1)
  resume=models.FileField()

class Analysis(models.Model):
  user_id=models.ForeignKey(User, on_delete=CASCADE,default=1)
  score=models.IntegerField()
  max_score=models.IntegerField()
  precentage=models.FloatField()
  status=models.CharField(max_length=20)
  date=models.DateField()
  



