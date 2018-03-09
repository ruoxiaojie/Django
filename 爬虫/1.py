#!/usr/bin/python3.5
# Author: xiaojie
import requests
from bs4 import BeautifulSoup


from multiprocessing import Process,Queue
import time,random,os


def consumer(q):
    while True:
        time.sleep(random.randint(1,3))
        res=q.get()
        if res is None:break
        print('\033[45m消费者拿到了：%s\033[0m' %res)

def producer(seq,q):
    for item in seq:
        time.sleep(random.randint(1,3))
        print('\033[46m生产者生产了：%s\033[0m' %item)

        q.put(item)

if __name__ == '__main__':
    q=Queue()

    c=Process(target=consumer,args=(q,))
    c.start()

    producer(('包子%s' %i for i in range(10)),q)
    q.put(None)
    c.join()
##主进程等待p结束，p等待c把数据都取完，c一旦取完数据,c.join就是不再阻塞,进
#而主进程结束,主进程结束会回收守护进程c,而且c此时也没有存在的必要了
    print('主线程')

'''
生产者生产了：包子0
消费者拿到了：包子0
生产者生产了：包子1
消费者拿到了：包子1
生产者生产了：包子2
消费者拿到了：包子2
生产者生产了：包子3
消费者拿到了：包子3
生产者生产了：包子4
消费者拿到了：包子4
生产者生产了：包子5
消费者拿到了：包子5
生产者生产了：包子6
消费者拿到了：包子6
生产者生产了：包子7
消费者拿到了：包子7
生产者生产了：包子8
消费者拿到了：包子8
生产者生产了：包子9
消费者拿到了：包子9
主线程
'''
