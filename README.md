# Unisport Code Challenge
## Installation
Working Ubuntu installation process

First, check if da_DK.UTF-8 locale is already in the system with:
```bash
$ locale -a
```
If it is not in the list, do:
```bash
$ sudo locale-gen da_DK.UTF-8
$ sudo update-locale
```

Once the locale is installed on the system:
```bash
$ sudo pip install virtualenv
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=challenge.py

```

## Usage
```bash
$ . venv/bin/activate # (Only if it was deactivated before)
$ flask run

```

## Testing

```bash
$ python -m unittest discover
```

## Check the code follows PEP 8 convention
```bash
$ pep8 *.py
```

## Live demo at Heroku

[Click here for a demo](https://arcane-ridge-72669.herokuapp.com/products/) running the [heroku branch](https://github.com/Delape/sample/tree/heroku)

This branch does not use SQLite. The reason behind this is because Heroku's filesystem.
More information can be found on [this article.](https://devcenter.heroku.com/articles/sqlite3)

In a production enviroment I would use PostgreSQL but I decided to use SQLite in this case because it is fair simple to use and it already comes with python.

## API

#### GET Method

##### `/products/`

Returns first 10 products ordered by price (ascending)

##### `/products/?page=n`

Returns paginated content where `n` is the number of the page

##### `/products/id/`

Returns a product by its `id`

##### `/products/kids/`

Returns all products marked for `kids` ordered by price (ascending)

#### DELETE Method
##### `/products/id/`

Deletes a product by its `id`

#### Example using `curl`

##### `Retrieving the product with id=1`

curl -i https://arcane-ridge-72669.herokuapp.com/products/1/
