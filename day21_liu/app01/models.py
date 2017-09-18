from django.db import models

# Create your models here.

class Depart(models.Model):
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32) # admin,ModelForm
    phone = models.CharField(max_length=32)
    dp = models.ForeignKey(to='Depart',to_field='id')
