
This is a fork of unisport sample task.
A data benchmark can be found [here](http://www.unisport.dk/api/sample/).

To prepare the application you have to do the following steps.

First clone this repository.

Create virtual environment `mkvirtualenv sample`

Run `pip install -r requirements.txt`

Run `python setup.py develop`

Optionally you can run tests `py.test`

Finally, you can start the service `./start.sh`

**IMPORTANT: please note you need to have sqlite3 installed on your system.**

The following endpoints are available now.

**/products/**

Returns the first 10 objects ordered with the cheapest first.
 
**/products/kids/**

Returns the products where kids=1 ordered with the cheapest first

**/products/?page=2** 

Returns correspondent page of products. Each page has 10 items.   

**/products/id/**

Returns the individual product.