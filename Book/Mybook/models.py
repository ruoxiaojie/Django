from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    price = models.FloatField()
    date = models.DateField()
    publish = models.CharField(max_length=32)
    describe = models.CharField(max_length=500)