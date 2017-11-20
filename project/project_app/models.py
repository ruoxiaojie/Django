from django.db import models

class User(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)

class Host(models.Model):
    ip = models.GenericIPAddressField(max_length=16)
    name = models.CharField(max_length=16)
    class Meta:
        verbose_name_plural = "主机表"
    def __str__(self):
        return self.ip

class Tomcat(models.Model):
    name = models.CharField(max_length=16)
    tomcat_name = models.CharField(max_length=64)
    domain_name = models.CharField(max_length=64)
    project_path = models.CharField(max_length=64)
    tomcat_path = models.CharField(max_length=64)
    host = models.ManyToManyField(verbose_name='所在主机', to='Host', blank=True)

    class Meta:
        verbose_name_plural = "应用表"
    def __str__(self):
        return self.name

