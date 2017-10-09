#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

import hashlib

def encrypt(pwd):
    obj = hashlib.md5()
    obj.update(pwd.encode('utf-8'))
    res = obj.hexdigest()
    return res