from django.db import models

#用户
class UserInfo(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.EmailField(null=True)
    services = models.ManyToManyField('UserHost')
#主机
class HostInfo(models.Model):
    name = models.CharField(max_length=16)
    ip = models.CharField(max_length=16)
    port = models.CharField(max_length=8)
    userhost = models.ForeignKey('UserHost')


#关系
class UserHost(models.Model):
    name = models.CharField(max_length=16)
