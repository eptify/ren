grammar:
	python setup.py grammar

coverage:
	pytest --quiet --cov=ren --cov-report=html

test:
	tox

lint:
	flake8 setup.py ren/*.py tests/*.py
