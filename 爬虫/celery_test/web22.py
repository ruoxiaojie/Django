#!/usr/bin/python3.5
import time
from celery import Celery
app = Celery()
app.config_from_object("celeryconfig")

@app.task
def taskA(x,y):
    return x * y

@app.task
def taskB(x,y,z):
    return x + y + z

# @app.task
# def add(x,y):
#     return x + y

