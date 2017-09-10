from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField(null=True)
    services = models.ManyToManyField('ServiceLine')

class HostInfo(models.Model):
    name = models.CharField(max_length=64)
    ip = models.CharField(max_length=64)
    port = models.CharField(max_length=64)
    service_line = models.ForeignKey('ServiceLine')



class ServiceLine(models.Model):
    name = models.CharField(max_length=64)


class Searchpoint(models.Model):
    name = models.CharField(max_length=300)











