from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=32)
    price=models.IntegerField()
    author=models.CharField(max_length=32)
    publiosh=models.CharField(max_length=32)