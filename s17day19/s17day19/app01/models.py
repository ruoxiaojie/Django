from django.db import models

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField(null=True)

class Host(models.Model):
    hostname = models.CharField(max_length=32)
    port = models.CharField(max_length=10)
