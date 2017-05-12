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

**** -------------------------------------------------------------------------------------------***
**** -------------------------------------------------------------------------------------------***
**** -------------------------------------------------------------------------------------------***
**** -------------------------------------------------------------------------------------------***

This sample project is implemeted using 
	.) PyCharm as the IDE
	.) Python version 3.6
	.) Django version 1.11.1 as the web framework
	.) SQLite3 as the database
	.) Bootstrap 3 as front-end framework
	
I have chosen Django due to have none of experience in making a website with Python. The google results of python web framework shows that
Django is one of the most popular and powerful web framework and it works based on MVC pattern. 

SQLite3 comes along with Django when installed. Due to the specification requirements there is necessarily only one relation (table) in the database.
Therefore SQLites3 is much more lightweight. 

As running the server "localhost". The main url is: "http://127.0.0.1:8000/products/"
The local folder has the link: "~\Desktop\Uniwebsite\"