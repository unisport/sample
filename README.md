In my solution the main Webservice file routes the requests using Flask.

The code is structured into classes, so it is easier to switch between data sources and change the way the data is sorted and manipulated if needed, before the data is returned.

Files:
  WebserviceUnisportData.py:
    contains: webservice checks the url for variables and routes the request. Return the data as json 
  GetData.py:
    contains: functions for getting data from Unisport json sample data or other sources of data
  SortData.py:
    contains: functions for sorting the data fetched from unisport sample data or other sources
  ManipulateData.py:
    contains: functions to create, update and delete products in unisport sample data



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

#### Bonus:
 extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._  

#### Forking and Pull Requests
Information on how to work with forks and pull requests can be found here https://help.github.com/categories/collaborating-with-issues-and-pull-requests/
