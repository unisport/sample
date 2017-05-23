.PHONY: coverage lint setup test

coverage:
				coverage run tests.py
				coverage report -m

lint:
				pep8 *.py

setup:
				pip install -r requirements.txt

test:
				python tests.py
