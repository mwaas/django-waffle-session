distribute:
	@python setup.py sdist

test:
	pip install -r requirements.txt && ./run.sh test
