# API documentation

The project runs on Python/Django and it's using Docker for the infrastructure.

I chose Docker because it keeps the project portable and easy to run/deploy
I was already familiar with Python and Django so that was my go to.

The project also uses Django REST framework as an additional layer to structure the API.

To run the project simply clone the repo and run _docker-compose up_ from a command line.
After it's done run _docker-compose exec api python api/importer.py_
This command will get the data from [Unisport's API](https://www.unisport.dk/api/products/batch/) and save it to the database instance.
Once the data is loaded from the API into the database all the endpoints will work fine.

I decided to use a database because all the operations are much faster than parsing the data on the fly.
Postgress is particularly indicated to handle complex structures like JSON and arrays.

The API will expose:

**/api/products/**
Will return all the product's list paginated by 10 items per page, ordered by price (ascending)

**/api/products/?page=x**
Will return the X page number of the product's list

**/api/products/id**
Will return a single product based on it's id

**/api/products/age**
Will return a list of products based the _age_ filter: it takes **kids** or **adults** as parameter.

The API will accept all the CRUD operations and it's REST based.

_GET_ _PATCH_ _DELETE_ _PUT_ will work on **/api/products/id**
_GET_ _POST_ will work on **/api/products/**
