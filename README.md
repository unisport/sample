# sample_for_unisport

[![build-status-image]][travis]
[![pypi-version]][pypi]

## Overview

Your project description goes here

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7)
* Django REST Framework (2.4.3, 2.4.4, 3.0-beta)

## Installation

Install using `pip`...

```bash
$ pip install sample_for_unisport
```

## Example

TODO: Write example.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```


[build-status-image]: https://secure.travis-ci.org/olmar/sample_for_unisport.png?branch=master
[travis]: http://travis-ci.org/olmar/sample_for_unisport?branch=master
[pypi-version]: https://pypip.in/version/sample_for_unisport/badge.svg
[pypi]: https://pypi.python.org/pypi/sample_for_unisport

_Fork this project and send us a pull request_

Write a simple python webservice that returns the objects & manipuates the data found here [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).


**/products/**


should return the first 10 objects ordered with the cheapest first.

**/products/kids/**

should return the products where kids=1 ordered with the cheapest first

**/products/?page=2**

 The products should be paginated where **page** in the url above should return the next 10 objects

 **/products/id/**

should return the individual product.



**_Remember to test_**
**_Remember to document (why, not how)_**

####Bonus:
 extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._

