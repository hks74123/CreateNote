from django.db import models


class mynt(models.Model):
    Title=models.CharField(max_length=150)
    Tag=models.CharField(max_length=500)
    Note=models.TextField()