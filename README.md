## README

## Introduction

Two solutions have been provided:
- RestAPI: Using the Django REST API Framework to allow create, retrieve, update, delete functionality
- Web: A Django views web interface that allows display of products, product detail and deletion. Uses bootstrap 5.

## Prerequisites

Poetry is used for managing dependencies and building a python source distribution and pure wheel.

Instructions for installing poetry are provided [here](https://python-poetry.org/docs/#installation)


## Getting Started

A Makefile has been provided to simplify setup and development.

1. Download poetry, details are provided in the prerequisites section above
2. Download data and create admin user: `make setup`
3. Create an admin user: `make createsuperuser`
4. Run Tests: `make test`
5. Run Server: `make run`

In a browser try out the following webviews:
- http://localhost:8000/products?page=1
- http://localhost:8000/products/<id>


## Swagger OpenAPI Documentation

Swagger documentation for the Rest API solution can be found by visiting http://localhost:8000/api/schema/swagger-ui/
This documents the RestAPI endpoints for creating, fetching, updating and deleting products.

## Webviews

The following web views are available:
- http://localhost:8000/products?page=1
- http://localhost:8000/products/<id>


## Development Tool Summary

- Uses flake8 linter to enforce code style and reduce errors before commit.
- Uses black code and isort formatting tools to automate formatting of code, such as alphabetic ordering of imports etc.
- Uses pre-commit to install hooks to run linting and code formatting before local commits
- Uses bootstrap 5 to render templates for Django views

## Docker

A docker-compose stack has been provided. To run in docker, issue the following command:

```
make up
```

This will build a docker image. On startup the docker container will create a default user of
`admin` with a password of `Pa55w0rd`. The `.env-sample` file in the root folder contains configuration
variables for the docker environment. Rename this file to `.env` for docker-compose to use
the environment variables to configure the containers.

```
DJANGO_DEBUG=True
DJANGO_EXT_PORT=5000
DJANGO_SECRET_KEY=Pa55w0rd
DJANGO_SUPERUSER_EMAIL=me@example.com
DJANGO_SUPERUSER_PASSWORD=Pa55w0rd
DJANGO_SUPERUSER_USERNAME=admin
NGINX_EXT_PORT=8000
```

## The Technical Test Assignment 

_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [https://www.unisport.dk/api/products/batch/](https://www.unisport.dk/api/products/batch/?list=200776,213591,200775,197250,213590,200780,209588,217706,205990,212703,197237,205989,211651,213626,217710,200783,213576,202483,200777,203860,198079,189052,205946,209125,200784,190711,201338,201440,206026,213587,172011,209592,193539,173432,200785,201442,203854,213577,200802,197362).


**/products/**  


should return the first 10 objects ordered with the cheapest first.

**/products/?page=2**
 
 The products should be paginated where **page** in the url above should return the next 10 objects  

 **/products/id/**
 
should return the individual product.


 
**_Remember to test_** 
**_Remember to document (why, not how)_**

#### Bonus:
 extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._  

#### Forking and Pull Requests
Information on how to work with forks and pull requests can be found here https://help.github.com/categories/collaborating-with-issues-and-pull-requests/

