#!/usr/bin/python3.5
import time
from web22 import *

# import sys
# print(sys.path)

time.sleep(1)
r1 = taskA.delay(10,20)
time.sleep(1)
print(r1.result)
print(r1.status)
time.sleep(1)
r2 = taskB.delay(10,20,30)
time.sleep(1)
print(r2.status)
print(r2.result)