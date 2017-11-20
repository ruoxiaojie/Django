from django.db import models

# Create your models here.

class Host(models.Model):
    ''''''
    ip=models.GenericIPAddressField(verbose_name='IP地址',max_length=16)
    ssh_port=models.CharField(verbose_name='ssh端口',max_length=6)
    name=models.CharField(verbose_name='用户',max_length=16)
    server_model=models.CharField(verbose_name='服务器型号',max_length=16)
    service=models.ForeignKey(Service)


class Service(models.Model):
    service_type=models.CharField(verbose_name='服务',max_length=16)
