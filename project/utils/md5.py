#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

import hashlib
def my_md5(pwd):
    import hashlib
    obj=hashlib.md5()
    obj.update(pwd.encode('utf-8'))
    data=obj.hexdigest()
    return data