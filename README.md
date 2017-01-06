####About the project: 
 Simple API for unisport assignment.

####Requirements: 
 Project is written in Flask framework. Project is runed in virtual environment. Link to how to install virtualenvironment http://flask.pocoo.org/docs/0.10/installation/


###Instalation: 
 In order to run the project following python packages MUST be installed. 
* pip install Flask 
* pip install requests 
* pip install sqlalchemy


After installing the packages pleas clone the project to the app directory so your final structure of your catalogs will look like this
* /unisport
* /unisport/app (clone git here)
* /unisport/venv


####Resource: 
 In order to facilitate testing a Postman collection has been created and can be reached from this [postman collection]( https://www.getpostman.com/collections/9a5dc18a9829ffffb274) link to [postman plugin](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en)


####Original requirements:
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

