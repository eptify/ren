grammar:
	python setup.py grammar

test:
	pytest --cov=ren --cov-report=html

lint:
	flake8 setup.py ren/*.py tests/*.py
