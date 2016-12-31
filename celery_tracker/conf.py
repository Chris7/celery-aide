import os

CELERY_TRACKER_QUEUE = os.environ.get('CELERY_TRACKER_QUEUE', 'celery_tracker')