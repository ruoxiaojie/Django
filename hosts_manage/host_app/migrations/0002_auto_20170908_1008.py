# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('port', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Yewu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='host',
            field=models.ManyToManyField(to='host_app.Host'),
        ),
        migrations.AddField(
            model_name='user',
            name='yewu',
            field=models.ManyToManyField(to='host_app.Yewu'),
        ),
    ]