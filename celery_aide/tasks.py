from celery import Celery
from celery.states import state, PENDING

from .models import CeleryTask

app = Celery('celery_aide')

@app.task
def task_update(task_id=None, task_args=None, task_extra=None, task_kwargs=None, task_name=None, task_queue=None, task_state=None):
  task, created = CeleryTask.objects.get_or_create(task_id=task_id)
  if not created:
      # if we are not the first one here, we only want to update if we are at a state with higher precedence
      if state(task_state) < state(task.state):
          if task.queue is None and task_queue is not None:
              task.queue = task_queue
              task.save()
          return
  if task_args:
      task.args = task_args
  if task_extra:
      task.extra = task_extra
  if task_kwargs:
      task.kwargs = task_kwargs
  if task_name:
      task.name = task_name
  if task_queue:
      task.queue = task_queue
  if task_state:
      task.state = task_state
  else:
      if task.state is None:
          task.state = PENDING
  task.save()
