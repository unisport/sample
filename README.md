# Installation
1. `git clone https://github.com/nielslerches/sample`
2. `cd sample`
3. macOS & Linux: `. venv/bin/activate` / Windows: `venv\Scripts\activate`
4. `pip install -r requirements.txt`

# Running
1. `cd sample`
2. macOS & Linux: `. venv/bin/activate` / Windows: `venv\Scripts\activate`
3. `python main.py`
The server is now running on `127.0.0.1:5000`

---
# Original README:

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
