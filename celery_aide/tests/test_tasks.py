import uuid

from celery import states
from django.test import TestCase

from celery_aide import tasks
from celery_aide.models import CeleryTask

class TaskTests(TestCase):
    def setUp(self):
        self.task_id = str(uuid.uuid4())
        self.task_name = 'test_task'
        self.initial_state = states.PENDING
        self.task_queue = 'test_queue'

    def test_task_update(self):
        tasks.task_update(
            task_id=self.task_id,
            task_name=self.task_name,
            task_queue=self.task_queue,
        )
        CeleryTask.objects.get(task_id=self.task_id)

        # Test updates
        new_state = states.STARTED
        tasks.task_update(
            task_id=self.task_id,
            task_name=self.task_name,
            task_state=new_state
        )

        task = CeleryTask.objects.get(task_id=self.task_id)
        self.assertEqual(task.state, new_state)

        # Make sure we do not update with a lesser state
        tasks.task_update(
            task_id=self.task_id,
            task_name=self.task_name,
            task_state=states.PENDING
        )

        task = CeleryTask.objects.get(task_id=self.task_id)
        self.assertEqual(task.state, new_state)

    def test_task_queue_update(self):
        # If a postrun task is processed before the prerun, we
        # can end up with an update from a state with lower
        # precedence having important information. Make sure we
        # update these cases
        tasks.task_update(
            task_id=self.task_id,
            task_name=self.task_name,
            task_state=states.SUCCESS
        )
        task = CeleryTask.objects.get(task_id=self.task_id)
        self.assertEqual(task.queue, None)

        new_queue = 'new_test_queue'
        tasks.task_update(
            task_id=self.task_id,
            task_queue=new_queue,
            task_state=states.PENDING
        )
        task = CeleryTask.objects.get(task_id=self.task_id)
        self.assertEqual(task.queue, new_queue)