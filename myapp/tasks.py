# myapp/tasks.py
from celery import shared_task
import time

@shared_task
def print_hello_world():
    print("Hello, World!")
