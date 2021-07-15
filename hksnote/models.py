from django.db import models
from django.contrib.auth.models import User

class mynt(models.Model):
    tid = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    Title=models.CharField(max_length=150)
    Tag=models.CharField(max_length=500)
    Note=models.TextField()
