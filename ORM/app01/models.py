from django.db import models

# Create your models here.

class Book(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=6,decimal_places=2)  #一共6位 xxxx.xx
    publisher=models.ForeignKey("publish")
    #外键建在一对多的 多的表中  建在子表
    aushor=models.ManyToManyField("Author") #创建的第三张表

class publish(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField(max_length=32)
    def __str__(self):
        return self.name

class Author(models.Model):
    name=models.CharField(max_length=32)

