_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [https://www.unisport.dk/api/products/batch/](https://www.unisport.dk/api/products/batch/?list=179249,179838,174351,180011,180020,178429).


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
