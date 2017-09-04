from django.db import models

# Create your models here.

class User(models.Model):
    '''用户登入系统表'''
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)