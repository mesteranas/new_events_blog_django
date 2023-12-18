from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile (models.Model):
    bio=models.TextField(default="")
    gender=models.TextField(default="")
    postsCount=models.IntegerField(default=0)
    user=models.OneToOneField(User,models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.user.first_name,self.user.last_name)
class post(models.Model):
    title=models.CharField(max_length=500)
    body=models.TextField()
    resources=models.TextField()
    date=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    is_view=models.BooleanField(default=False)
    like=models.IntegerField(default=0)
    deslike=models.IntegerField(default=0)
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.title
