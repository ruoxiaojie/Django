#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
from django.shortcuts import HttpResponse,redirect

def Auth(func):
    def wrapper(request,*args,**kwargs):
        session_dict = request.session.get('user_info')
        if session_dict:
            res = func(request,*args,**kwargs)
            return res
        else:
            return redirect('/login')
    return wrapper