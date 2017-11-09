from django.db import models


class User(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.EmailField(verbose_name='邮箱')
    roles = models.ManyToManyField(verbose_name='拥有角色', to='Role', blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色表 --
    """
    caption = models.CharField(verbose_name='角色', max_length=32)

    permissions = models.ManyToManyField(verbose_name='拥有权限', to='Permission', blank=True)

    def __str__(self):
        return self.caption


class Menu(models.Model):
    """
    菜单表
    """
    caption = models.CharField(verbose_name='菜单名称', max_length=32)
    is_group = models.BooleanField(verbose_name='是否为组', default=False)
    parent = models.ForeignKey('self', verbose_name='父菜单', related_name='p', null=True, blank=True,
                               limit_choices_to={'is_group': False})

    def __str__(self):
        menu_list = [self.caption, ]
        parent = self.parent
        while True:
            if parent:
                menu_list.append(parent.caption)
                parent = parent.parent
            else:
                break
        menu_list.reverse()
        return '-'.join(menu_list)


class Permission(models.Model):
    """
    权限URL
    """
    caption = models.CharField(verbose_name='权限名称', max_length=32)
    url = models.CharField(verbose_name='URL', max_length=128, null=True, blank=True)
    code = models.CharField(verbose_name='权限代码', max_length=64)
    is_menu = models.BooleanField(verbose_name='是否为菜单', default=False)
    group = models.ForeignKey(
        verbose_name='所属组',
        to="Menu",
        related_name='permissions',
        limit_choices_to={'is_group': True}
    )

    def __str__(self):
        return "%s" % (self.caption,)
