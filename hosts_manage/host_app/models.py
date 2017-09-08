from django.db import models

# Create your models here.


class Yewu(models.Model):
    name=models.CharField(max_length=32)

class Host(models.Model):
    '''主机表'''
    ip=models.GenericIPAddressField()
    port=models.CharField(max_length=6)

class User(models.Model):
    '''用户登入系统表'''
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    email=models.EmailField(null=True)
    yewu=models.ManyToManyField("Yewu")
    host=models.ManyToManyField("Host")







