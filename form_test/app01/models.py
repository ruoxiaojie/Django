from django.db import models

# Create your models here.


class Depart(models.Model):
    title = models.CharField(max_length=32)

class UserIofo(models.Model):
    name =models.CharField(max_length=32)
    email = models.EmailField(max_length=32) #EmailFiled  admin 用到
    phone = models.CharField(max_length=32)
    dp =models.ForeignKey(to='Depart',to_field='id')
