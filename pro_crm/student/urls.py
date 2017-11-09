#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url,include
from arya.service.sites import site
from . import views
urlpatterns = [
    url(r'^login/', views.login),
    url(r'^index/', views.index),
    url(r'^evaluate/(\d+)/(\d+)/', views.evaluate),
]