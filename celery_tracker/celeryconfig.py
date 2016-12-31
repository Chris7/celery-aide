import os

from kombu import Queue

from . import conf

broker_url = os.environ.get('BROKER_URL', 'amqp://guest:guest@localhost:5672//')
imports = ('celery_tracker.tasks')
task_ignore_result = True

task_queues = (
    Queue(conf.CELERY_TRACKER_QUEUE, routing_key='{}.#'.format(conf.CELERY_TRACKER_QUEUE)),
)