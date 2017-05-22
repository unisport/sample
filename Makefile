.PHONY: coverage lint setup test

coverage:
				coverage run tests.py
				coverage report -m

lint:
				pep8 tests.py
				pep8 unisport.py

setup:
				pip install -r requirements.txt

test:
				python tests.py
