#!/usr/bin/python3.5

from kombu import Queue,Exchange
BROKER_URL = "redis://10.211.55.9:6379/1"
CELERY_RESULT_BACKEND = "redis://10.211.55.9:6379/2"

CELERY_QUEUES = {
    Queue("default",Exchange("default"),routing_key="default"),
    Queue("for_task_A",Exchange("for_task_A"),routing_key="for_task_A"),
    Queue("for_task_B",Exchange("for_task_B"),routing_key="for_task_B"),
}

CELERY_ROUTES = {
    "web22.taskA":{"queue":"for_task_A","routing_key":"for_task_A"},
    "web22.taskB":{"queue":"for_task_B","routing_key":"for_task_B"},
}