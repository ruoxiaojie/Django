# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-30 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20171030_0905'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role2permission',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='role2permission',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='role2permission',
            name='role',
        ),
        migrations.AlterUniqueTogether(
            name='useraction',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='useraction',
            name='action',
        ),
        migrations.RemoveField(
            model_name='useraction',
            name='role_permission',
        ),
        migrations.DeleteModel(
            name='Role2Permission',
        ),
        migrations.DeleteModel(
            name='UserAction',
        ),
    ]
