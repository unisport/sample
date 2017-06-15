# README #
Webservice created using Django.

## /products/ ##
###Task description###
*Should return the first 10 objects ordered with the cheapest first.*
###My solution###
Reads the data from the url and uses the python function sorted, to manipulate the list.

Uses Paginator to show 10 items on each page, until there are no more pages. See https://docs.djangoproject.com/en/1.11/topics/pagination/ for documentation.
## /products/kids ##
###Task description###
*Should return the products where kids=1 ordered with the cheapest first*
###My solution###
Created a new list 'product_list_kids', that was true to the condition. Then uses Paginator the same way, as with products.
## /products/?page=2 ##
###Task description###
*The products should be paginated where page in the url above should return the next 10 objects*
###My solution###
Done by using Paginator.
## /products/id ##
###Task description###
*Should return the individual product.*
###My solution###
Search through the 'product_list', for the item that had the same value. In id.html there is a special case, for the instance where the ID does not exist.
## Tests ##
All tests can be found in tests.py.
The tests primarily ensures that the correct items are displayed within the various urls.