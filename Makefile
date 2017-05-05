grammar:
	python setup.py grammar

test:
	pytest --cov=ren --cov-report=html
