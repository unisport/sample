.PHONY: coverage lint setup migrate test

coverage:
				coverage run tests.py
				coverage report -m

lint:
				pep8 *.py

setup:
				pip install -r requirements.txt

migrate:
				python dbmigrator.py

test:
				python tests.py
