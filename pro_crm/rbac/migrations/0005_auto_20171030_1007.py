# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20171030_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='url',
        ),
        migrations.AddField(
            model_name='permission',
            name='pre_url',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='permission',
            name='caption',
            field=models.CharField(max_length=32, verbose_name='权限前缀'),
        ),
    ]
