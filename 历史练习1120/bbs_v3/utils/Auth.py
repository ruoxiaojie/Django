#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse

def auth(func):
    def wrapper(request,*args,**kwargs):
        session_dict = request.session.get('is_login')
        if session_dict:
            res = func(request,*args,**kwargs)
            return res
        else:
            return HttpResponse("操作前请先登录！")
    return wrapper