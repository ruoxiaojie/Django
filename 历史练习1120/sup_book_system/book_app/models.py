from django.db import models

# Create your models here.
#每个class都是一张表
class Publisher(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=50)


class Book(models.Model):
    title=models.CharField(max_length=100)
    publication_date=models.DateField()
    price=models.DecimalField(max_digits=5,decimal_places=2,default=10)
    publisher=models.ForeignKey(Publisher)
