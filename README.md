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


####Installation:
pip install -r requirements.txt

#### Run:
python run.py 

it should start service on localhost:5000

### Try it:
curl -X GET http://localhost:5000/products/
curl -X GET http://localhost:5000/products/kids/
curl -X GET http://localhost:5000/products/103897/
curl -X DELETE http://localhost:5000/products/103897/
curl -X PUT http://localhost:5000/products/1/?price=12
curl -X POST http://localhost:5000/products/1/?price=12
 
