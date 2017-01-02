testenv:
	pip install -r requirements.txt
	pip install -e .[django]

test:
	coverage run --append --branch --source=celery_aide `which django-admin.py` test --settings=celery_aide.test_settings celery_aide.tests
	coverage report

.PHONY: docs
docs:
	cd docs && make html
