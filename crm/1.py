#!/usr/bin/python
# Author:xiaojie
# -*- coding:utf-8 -*-
import re


a = "狙击精英：巅峰对决[HD-720P-MP4][中英双字]"
b =re.findall('(\S*)\[.*\]\[.*\]',a)[0]
print(b)

# \[









