from django.db import models

class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)

class Role(models.Model):
    caption = models.CharField(max_length=32)

class UserInfo(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    ut = models.ForeignKey(UserType,null=True,blank=True)
    rl = models.ManyToManyField(Role)

# obj = UserInfo()
# obj.r1.values('id','caption') # [Role,ROle]