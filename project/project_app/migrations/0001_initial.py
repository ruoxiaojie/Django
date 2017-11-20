# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': '主机表',
            },
        ),
        migrations.CreateModel(
            name='SoftWare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('domain_name', models.CharField(max_length=64)),
                ('project_path', models.CharField(max_length=64)),
                ('tomcat_path', models.CharField(max_length=64)),
                ('host', models.ManyToManyField(blank=True, to='project_app.Host', verbose_name='所在主机')),
            ],
            options={
                'verbose_name_plural': '应用表',
            },
        ),
    ]