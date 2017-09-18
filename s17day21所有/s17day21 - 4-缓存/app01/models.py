from django.db import models

class Depart(models.Model):
    """
    部门表
    """
    title = models.CharField(max_length=32) # 数据中的string类型

class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32) # admin,ModelForm，数据中的string类型
    phone = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    dp = models.ForeignKey(to='Depart',to_field='id')
