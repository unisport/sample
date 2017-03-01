Coding Challenge
===================

Installation
----------------
To install clone the repository and cd into the the  ``sample`` directory.

To install using `virtualenv`
```sh
$ virtualenv --no-site-packages ~/.Virtualenv/sampleenv
$ source ~/.Virtualenv/sampleenv/bin/activate
```
To install project requirements:
```sh
$ pip install -r requirements/local.pip
```
The application runs using ``sqlite3`` database. To use ``postgresql`` :

```sh
$ pip install psycopg2
```
```sh
$ psql createdb databasename
```
And change the the database settings in
 ``unisport/settings/local.py``
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'databasename',
        'PORT': 5432,
        'HOST': 'localhost',
        'USER': 'your_database_username',
    }
}

```
To set up database run:
```sh
$ ./manage.py makemigrations
$ ./manage.py migrate
```

Create an admin account.
```sh
$ ./manage.py createsuperuser
```

To run the backend application:
```sh
$ ./manage.py runserver_plus
```

The backend application will be accessible at: http://127.0.0.1:8000/api/products/

To install frontend app dependencies:
```sh
$ npm install -g grunt-cli
$ npm install
$ bower install
```

To run the frontend application run in a new terminal window:
```sh
$ grunt serve
```

The application will be accessible at: http://localhost:9000/


Settings
------------

When using https://www.unisport.dk/api/sample/
``DATA_SOURCE = "external"`` in ``unisport/settings/base.py``
To use database as data source ``DATA_SOURCE = "internal"``

To import data from https://www.unisport.dk/api/sample/
```sh
$ ./manage.py import_data
``` 

To test the backend applicatio
```sh
$ ./manage.py test
```
