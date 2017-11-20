#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
from django.views import View
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.shortcuts import redirect
class AuthView(View):
    '''用户认证'''
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        if request.session.get('user_info'):
            response = super(AuthView,self).dispatch(request,*args,**kwargs)
            return response
        else:
            return redirect('/login.html')