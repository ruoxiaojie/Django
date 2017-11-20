from django.db import models

# Create your models here.

class UserType(models.Model):
    title = models.CharField(max_length=32)

class Role(models.Model):
    caption=models.CharField(max_length=32)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    ut = models.ForeignKey(UserType,null=True,blank=True)
    rl = models.ManyToManyField(Role)