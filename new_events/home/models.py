from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile (models.Model):
    bio=models.TextField(default="")
    gender=models.TextField(default="")
    postsCount=models.IntegerField(default=0)
    user=models.OneToOneField(User,models.CASCADE)
