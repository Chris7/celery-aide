# Celery-Aide
A Django app which automatically keeps track of celery tasks run and allows for simple task resubmission and monitoring.

# Celery Integration

* Import signals when the Celery worker starts up
* The Django server and celery workers should share the same rabbit broker
