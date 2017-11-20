from django.db import models

# Create your models here.
#建立出版社表
class Publisher(models.Model):
    name = models.CharField("出版社名字",max_length=100)
    city = models.CharField('城市', max_length=60)
    state_province = models.CharField('省份',max_length=30)
    address = models.CharField("地址", max_length=50)


#建立书籍表
class Book(models.Model):
    title = models.CharField('书名',max_length=100)
    author = models.CharField('作者',max_length=100)
    publication_date = models.CharField('出版日期',max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    #(外键:一对多)
    pub = models.ForeignKey(to='Publisher',to_field='id')