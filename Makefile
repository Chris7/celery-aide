testenv:
	pip install -r requirements.txt
	pip install -e .

test:
	coverage run --append --branch --source=celery_tracker `which django-admin.py` test --settings=celery_tracker.test_settings celery_tracker.tests
	coverage report

.PHONY: docs
docs:
	cd docs && make html
