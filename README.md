# ![alt text](https://travis-ci.org/vaulor/Docker_test.svg?branch=master)
# ![alt text](https://unisport-assets.s3.amazonaws.com/styleguide/img/logo.svg "Unisport logo")   Unisport Code Challenge   ![alt text](https://unisport-assets.s3.amazonaws.com/styleguide/img/logo.svg "Unisport logo") 



## Installation
The following versions for docker and docker-compose are required to build and run the project.
```bash
Docker version 17.06.0-ce
docker-compose version 1.14.0
```

## Run

### Standalone docker container

There are several ways to run this project. If no dependencies other than docker
have to be met, there's an already built standalone image in docker to pull and run.

For this option run:
```bash
$ docker pull xavifdpcoorp/django_test:standalone_challenge_django_container
$ docker tag xavifdpcoorp/django_test:standalone_challenge_django_container standalone
$ docker run -p 8000:8000 standalone
```
Please note this container runs whith SQLite.

### Standalone docker stack

If there's the chance of using docker-compose, inside docker_compose_prebuild directory
it is a convenient docker-compose file to pull and run this django project container along
with an already built postgres docker image from Docker.

For this option run:
```bash
$ cd docker_compose_prebuild
$ docker-compose up
```
### Building docker image from source

And last but not least, there's the option of building the image of the development environment.
For this, it is a requirement to have docker-compose installed.

To build the development environment run:
```bash
$ cd django_test
$ docker compose up --build
```
While on development it is not required to build the image each time so the project can be
run without the `--build` option.

## Testing and style convention checking

```bash
$ cd django_test
$ pep8 --max-line-length=100 . && docker-compose run web python manage.py test products
```


## API

#### GET Method

##### `/products/`

Returns the cheapest 10 products ordered by price (ascending)

##### `/products/?page=n`

Returns paginated content where `n` is the number of the page ( 10 products per page )

##### `/products/id/`

Returns a product by its `id`

##### `/products/kids/`

Returns all products where field `kids` is true ordered by price (ascending)

#### POST Method
##### `/products/`
Creates the product sent( Only if its `id` doesn't exist already)

#### PUT Method
##### `/products/id/`
Updates or creates the product sent( Only if product `id` and endpoint match)

#### DELETE Method
##### `/products/id/`

Deletes a product by its `id`

#### Example using `curl`

##### `Retrieving the product with id=35608`

curl -i http://ec2-35-158-131-65.eu-central-1.compute.amazonaws.com/products/35608/


## Live demo at AWS ( Amazon Web Services )

[Click here for a demo](http://ec2-35-158-131-65.eu-central-1.compute.amazonaws.com/products/)

![alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/AmazonWebservices_Logo.svg/250px-AmazonWebservices_Logo.svg.png "AWS logo")
## Usage

There are plenty of tools to test APIs, but fortunately won't be necessary to test this webapp as django Rest Framework comes with
a nice and easy-to-use website tool.

When sending information to the web application, data must be sent in `application/json` media type.
That is, when copying a product information and pasting to content text area at the bottom of the page,
make sure to copy also the curly braces that enclose the information as a json.

#### GET
- To get the cheapest 10 products ordered by price go to /products/
- To get all producs marked as for kids go to /products/kids/ (May be there aren't, but can be created ;-) )
- To get another page of products other than the first one go to /products/?page=n ( where n is the page number)
- To get a certain product go to /products/id/ (where id is the product's id being looked for)

#### POST
- To post a product, from /products/ copy an already existing product and paste it in the text area named content.
Then change its `id` for another and click the blue bottom-right button `POST`

#### PUT
- To update an already existing product, go to /products/id/ (where id is product's id), copy the product and 
paste it in Content field. Afterwards modify one or more fields and click on the blue PUT button to the bottom-right.
- To create a new product through PUT method, remember that the id in the URL and the product's one must match.

#### DELETE
- To delete a product go to /products/id and click on the DELETE button on the top-right of the page.
