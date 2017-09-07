from django.db import models

# Create your models here.

class User(models.Model):
    '''用户登入系统表'''
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=64)
    email=models.EmailField(null=True)
    models.ManyToManyField(Host,Yewu)

class Host(models.Model):
    '''主机表'''
    ip=models.IPAddressField()
    port=models.CharField(max_length=6)


class Yewu(models.Model):
    name=models.CharField(max_length=32)

