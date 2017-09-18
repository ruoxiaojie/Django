from django.db import models

class Depart(models.Model):
    """
    部门表
    """
    title = models.CharField(max_length=32) # 数据中的string类型

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "部门表"

class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name
class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32) # admin,ModelForm，数据中的string类型
    phone = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    dp = models.ForeignKey(to='Depart',to_field='id')
    roles = models.ManyToManyField("Role")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "用户表"