Write a simple python webservice that returns the objects in data.json as json objects.


**/products/**  


should return the first 10 objects ordered by price=desc
 
**/products/?page=2**
 
 The products should be paginated where **page** in the url above should return the next 10 objects  

 **/products/id/**
 
should return the individual product
 
**_Remember to test_**   
**_Remember to document (why, not how)_**

####Bonus:
 extend the service so the products can also be created, edited and deleted.


_You are welcome to use any thirdparty python web framework that you are familier with._