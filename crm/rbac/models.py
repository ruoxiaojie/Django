from django.db import models

class Group(models.Model):
    #权限组
    title = models.CharField(max_length=32)
    parent = models.ForeignKey(to="Group",related_name='xx',null=True,blank=True)
    is_group = models.BooleanField(verbose_name="是否是组")
    class Meta:
        #admin 中文
        verbose_name_plural = "权限组表"
    def __str__(self):
        #创建的直接显示
        return self.title

class Permission(models.Model):
    #权限表
    title = models.CharField(verbose_name='标题',max_length=32)
    url = models.CharField(verbose_name='含正则的url',max_length=128)
    code = models.CharField(verbose_name='权限代号',max_length=16)
    group = models.ForeignKey(verbose_name='权限组',to='Group',limit_choices_to={'is_group':True})
    is_menu = models.BooleanField(verbose_name='是否菜单')
    class Meta:
        #admin 中文
        verbose_name_plural = "权限表"
    def __str__(self):
        #创建的直接显示
        return self.title

class UserInfo(models.Model):
    #用户表
    username = models.CharField(verbose_name='用户',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)
    roles = models.ManyToManyField(verbose_name='用户所有权限',to="Role",blank=True) #blank=True 取消必填
    class Meta:
        #admin 中文
        verbose_name_plural = "用户表"
    def __str__(self):
        #创建的用户直接显示
        return self.username

class Role(models.Model):
    #角色表
    title = models.CharField(verbose_name='角色名称', max_length=32)
    permissions = models.ManyToManyField(verbose_name='用户所有权限', to="Permission",blank=True)

    class Meta:
        #admin 中文
        verbose_name_plural = "角色表"
    def __str__(self):
        #创建的直接显示
        return self.title