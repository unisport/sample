I chose Django REST Framework for this webservice, because initial data was in JSON format and REST Framework has 
built-in opportunity to manipulate data in JSON format too.

Furthermore, REST Framework provides user interface for data creating, modifying and deletion both in html and 
json representations via generic class-based views.

As a database I used Postgres as usual choise for Python/Django web applications. To automate it's population 
I created a management command 'fetch_data' which import information from specified url source to database.

As price was formated according to Denmark standards, I set LANGUAGE_CODE to 'da-DK', so the application is able 
to consume and return data in native format.

Fields women, kids_adult and kids are seemed to be BooleanField and currency is seemed to be a ChoiseField, 
but that was not explicitly articulated, so for scratch I stopped with CharField. 

If I create them as I mentioned above, I will have to convert data from database boolean representation to 
explicit 0/1 format and here REST Framework comes with to_representation() and to_internal_value() methods.
==============================================================

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

