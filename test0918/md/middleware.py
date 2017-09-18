#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
from django.utils.deprecation import MiddlewareMixin

class M1(MiddlewareMixin):
    def process_request(self,request):
        print('m1.request')

    def process_response(self, request, response):
        print('m1.process')
        return response  #一定要有返回值


class M2(MiddlewareMixin):
    def process_request(self,request):
        print('m2.request')

    def process_response(self, request, response):
        print('m2.process')
        return response  #一定要有返回值