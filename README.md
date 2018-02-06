# My "simple" solution
## Layout
This app has been set up with extendability in mind. Therefore I choose to use a NGINX
server as a reverse proxy for the api. For serving static files (JavaScript and HTML)
I use NGINX. I choose this as Django is not suited for serving these files.

### Frontend
The frontend is made up of a React application. It is served by the NGINX server and makes
JavaScript requests to the backend to display the products. I choose React partly because
I know it well, partly because it is easy to make something good looking, and partly
because it is easy to maintain and test the code.

The frontend uses react-router to provide routing which means that the index.html file is
served to all urls except those which hosts files/API endpoints.

### Backend
The backend is made up of a Django project. I choose Django as it is easy to get up and
running and Django has a prebuilt admin interface, which makes it very easy to fulfill the
bonus "assignment".



## Setup
I am assuming this is run on a UNIX-like system. The reason is that I assume some basic
things to not overcomplicate the solution.

Programs needed to run the app:
- NGINX
- Python3 with requirements.txt installed
- Node.js and npm/yarn for the frontend

Run the setup.py script. If you have chosen the NGINX user to be other than http
you should change this in the script in line 14 in frontend/package.json.

To start the app start your NGINX server, start the Django server on port 8000 and
run `npm build` in the frontend directory.


# API
_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here:
[http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).

**/products/**

should return the first 10 objects ordered with the cheapest first.

**/products/kids/**

should return the products where kids=1 ordered with the cheapest first

**/products/?page=2**

The products should be paginated where **page** in the url above should return the next 10
objects

**/products/id/**

should return the individual product.


**_Remember to test_**
**_Remember to document (why, not how)_**

#### Bonus:
 -[x] extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._

#### Forking and Pull Requests
Information on how to work with forks and pull requests can be found here https://help.github.com/categories/collaborating-with-issues-and-pull-requests/
