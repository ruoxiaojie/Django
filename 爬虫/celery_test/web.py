#!/usr/bin/python3.5
import time
from xiaojie import add

a = add.delay(10,20)
print(a)
print(type(a))
time.sleep(1)
print(a.result)
print(a.status)
print(a.ready())
print(a.get(timeout=3))