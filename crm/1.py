#!/usr/bin/python
# Author:xiaojie
# -*- coding:utf-8 -*-

class A:  # 定义交通工具类
    def __init__(self, name):
        self.name = name
    def run(self):
        print('开动啦...')

class B(A):  # 地铁
    def __init__(self, name, line):
        # super(Subway,self) 就相当于实例本身 在python3中super()等同于super(Subway,self)
        super().__init__(name)
        self.line = line

    def run(self):
        print(self.line)
        super(B, self).run()


line13 = B('213', 'line')
line13.run()


