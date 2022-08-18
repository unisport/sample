export SRC=unisport


collectstatic:
	poetry run python manage.py collectstatic

lint:
	poetry run flake8 $(SRC)
	poetry run black --check --preview $(SRC)

pretty:
	poetry run isort $(SRC)
	poetry run black --preview $(SRC)

build:
	poetry build

run:
	poetry run python manage.py runserver

setup:
	@echo "Installing dependencies..."
	@poetry install
	@echo "Installing pre-commit git client hooks..."
	@poetry run pre-commit install
	@echo "Making migrations..."
	@poetry run python manage.py migrate
	@echo "Importing data..."
	@poetry run python manage.py dataimport
	@echo "Setup complete..."

dataimport:
	@poetry run python manage.py dataimport
	@echo "Setup complete..."

makemigrations:
	poetry run python manage.py makemigrations

createsuperuser:
	poetry run python manage.py createsuperuser

migrate:
	poetry run python manage.py migrate

removemigrations:
	poetry run python manage.py migrate unisport_data zero

showmigrations:
	poetry run python manage.py showmigrations

test: lint
	poetry run python manage.py test --parallel

wip:
	poetry run python manage.py test --tag=wip

up: dockerbuild
	docker-compose up

down:
	docker-compose down

dockerbuild:
	docker-compose build



