from django.db import models


class User(models.Model):
    '''uonghu登入表'''
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)

class SysTem(models.Model):
    name = models.CharField(max_length=16)
    class Meta:
        verbose_name_plural = "系统版本"
    def __str__(self):
        return self.name

class Host(models.Model):
    ip = models.GenericIPAddressField(max_length=16)
    hostname = models.CharField(max_length=16)
    system = models.ForeignKey(verbose_name='系统', to='SysTem', blank=True)
    class Meta:
        verbose_name_plural = "主机表"
    def __str__(self):
        return self.ip


class Application(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = "应用名称表"

    def __str__(self):
        return self.name


class APP(models.Model):
    name = models.ForeignKey(verbose_name='应用名称', to='Application')
    app_name = models.CharField(max_length=64)
    domain_name = models.CharField(max_length=64, blank=True)
    project_path = models.CharField(max_length=64, blank=True)
    app_path = models.CharField(max_length=64)
    host = models.ManyToManyField(verbose_name='所在主机', to='Host', blank=True)
    class Meta:
        verbose_name_plural = "应用详细表"
    def __str__(self):
        return self.name.name

