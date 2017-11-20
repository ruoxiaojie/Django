#!/usr/bin/python
# Author:xiaojie
# -*- coding:utf-8 -*-

import re

a = "sdweedefedfcdvda"

r = r"[sv]d[a-z]"
print(re.compile(r))
print(re.findall(r,a))













