Sample solution for given requirements
data for project read directly from [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).

**/products/**  
Returns the first 10 objects ordered with the cheapest first.
 
**/products/kids/** 
This sample solution has been made, so it tries matching the given string to a data paramter.
Returns only the data where to paramter is 1. (Works for women, kids, adult-kids)

**/products/?page=2** 
 The products should be paginated where **page** in the url above should return the next 10 objects  
And so it does.

 **/products/id/**
Returns the individual product.


The bonus questions have not been completed, as the data source was static.
The data could've been made local, editable or otherwise able to handle new input.
But has not been a priority, due to the time contraints.

This was made using Django 1.5.4 and Python 2.7.5

Error messages left on on purpose.