# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_app', '0002_auto_20171120_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomcat',
            name='tomcat_name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
