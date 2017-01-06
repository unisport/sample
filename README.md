_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).


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


####How to run:
1. create database in your favourite database server (I prefer Postgres);
2. copy local_settings.py.default to local_settings.py;
3. write your database settings into local_settings.py;
4. sync and migrate:
`python manage.py syncdb && python manage.py migrate`
5. run `python manage.py get_data` to get data from [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/);
6. run project `python manage.py runserver`.


**All actions described in this file above realized**
**Additionally realized creation, edition and delete products**

1. create product item:
`curl -X POST http://localhost:8000/products/ -data '{ \
    "kid_adult": "0", \
    "price": 79, \
    "delivery": "1-2 dage", \
    "women": "0", \
    "kids": "1", \
    "name": "Nike - T-Shirt Neymar Jr. Hero Grå Børn", \
    "package": "0", \
    "url": "http://www.unisport.dk/fodbold365/nike-t-shirt-neymar-jr-hero-gra-brn/119644/", \
    "free_porto": false, \
    "price_old": 199, \
    "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/119644_da_mellem.jpg" \
}'`
2. get product item data:
`curl -X GET http://localhost:8000/products/<product_id>/`
3. update product data:
`curl -X PATCH http://localhost:8000/products/<product_id>/ -data '{ \
    "kid_adult": "0", \
    "price": 79, \
    "delivery": "1-2 dage", \
    "women": "0", \
    "kids": "1", \
    "name": "Nike - T-Shirt Neymar Jr. Hero Grå Børn", \
    "package": "0", \
    "url": "http://www.unisport.dk/fodbold365/nike-t-shirt-neymar-jr-hero-gra-brn/119644/", \
    "free_porto": false, \
    "price_old": 199, \
    "img_url": "http://s3-eu-west-1.amazonaws.com/product-img/119644_da_mellem.jpg" \
}'`
4. delete product item:
`curl -X DELETE http://localhost:8000/products/<product_id>/`
