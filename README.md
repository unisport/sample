# Webservice for Unisport

## Overview
Simple python webservice that uses, manipulates and returns the data found here: http://www.unisport.dk/api/sample/.

## Installation
Install using pip : $pip install -r requirements.txt

### Web.py
The web service is based on webpy and implemented as follow:

* Run webservice.py in terminal: *python webservice.py*, this creates a web server on port 8080 to serve up the requests. Server is running at *localhost:8080* and endpoinds can be accessed by *localhost:8080/products/*

* The data is fetched from the api in the given link and saved to a json file in the same directory where webservice.py is excecuted.

* The endpoints are defined in url's and a class is assinged to each of them. Accessing the endpoints gives the results described below.

* The service returns JSON responses

## Endpoints
__/products/__

should return the first 10 objects ordered with the cheapest first.

__/products/kids/__

should return the products where kids=1 ordered with the cheapest first

__/products/?page=2__

The products should be paginated where page in the url above should return the next 10 objects

__/products/id/__

should return the individual product.
