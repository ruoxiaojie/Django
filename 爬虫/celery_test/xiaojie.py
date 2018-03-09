#!/usr/bin/python3.5



from celery import Celery
broker = 'redis://10.211.55.9:6379/5'
brokend = 'redis://10.211.55.9:6379/6'

app = Celery("xiaojie",broker=broker,backend=brokend)

@app.task
def add(x,y):
    return x+y



