# Sample webservice for Unisport

## Overview

Simple python webservice that returns the objects & manipuates the data found
here [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).


## Requirements

* Python 2.7
* Django 1.8
* Django REST Framework 3.1.1

## Installation

Install using `pip`...

```bash
$ pip install -r requirements.txt
```

## Endpoints

**/products/**


should return the first 10 objects ordered with the cheapest first.

**/products/kids/**

should return the products where kids=1 ordered with the cheapest first

**/products/?page=2**

 The products should be paginated where **page** in the url above should return the next 10 objects

 **/products/id/**

should return the individual product.


## Testing

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests. Simply run:

```bash
$ tox
```

## Documentation

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
