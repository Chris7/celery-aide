from django.apps import AppConfig


class CeleryTrackerConfig(AppConfig):
    name = 'celery_tracker'
    verbose_name = 'Celery Tracker'

    def ready(self):
        pass