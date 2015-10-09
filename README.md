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


####Requirements:
* Django=1.8.5

####Explanations:
 Data store in sqlite db. You can create new products or edit\delete existing using admin panel **/admin/**
 There wasn't any kids='1' objects in default data at this link:
* [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/) So i change one of them.

 Also You can clean the table and "reload" all default data using **Product.reload_data()** class method provided in products.models

####default SuperUser:
* login: **root**
* password: **qwerty**