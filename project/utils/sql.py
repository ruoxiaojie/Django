#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-

'''
#查看所有机器的系统
SELECT
  project_app_host.ip,
  project_app_system.name
FROM project_app_host
  LEFT JOIN project_app_system
    ON project_app_host.system_id = project_app_system.id AND project_app_system.name IN (SELECT project_app_system.name
                                                                                          FROM project_app_system);
'''
#恭贺小＋朋友们＝新年好

import random


def Sum(n):
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = random.sample(q, 3)
    q = list(set(q) ^ set(a))
    x = str(a[0]) + str(a[1]) + str(a[2])
    x = int(x)
    b = random.sample(q, 3)
    q = list(set(q) ^ set(b))
    y = str(b[0]) + str(b[1]) + str(b[2])
    y = int(y)
    c = random.sample(q, 3)
    z = str(c[0]) + str(c[1]) + str(c[2])
    z = int(z)
    if x + y == z:
        n = n+1
        print(x, y, z)
        print(n)
        Sum(n)
    else:
        Sum(n)

if __name__ == '__main__':
        n = 0
        Sum(n)







