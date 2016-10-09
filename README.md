
**Description**

This is a fork of unisport sample task. A data benchmark can be found [here](http://www.unisport.dk/api/sample/).

**Preparation of the application**

In order to prepare the application to be able to launch you have to do the following steps.

- First clone this repository.
- Create virtual environment `mkvirtualenv sample`
- Run `pip install -r requirements.txt`
- Run `python setup.py develop`
- Optionally you can run tests `py.test`
- Finally, you can start the service `./start.sh`

**IMPORTANT: please note you need to have sqlite3 installed on your system.**

**Data location**

By default the products you create or edit via web-page are strored in `data/products.db`. By default in `data` folder you can find the SQLite databse with data from [benchmark](http://www.unisport.dk/api/sample/).
If you'd like to use fresh db you need to remove `data/products.db` file and run `python createdb.py` to create a database schema.
If you'd like to fill fresh db with benchmark data go to examples folder and run `python migration.py` to migrate entries from `data.json` to `data/products.db` file.

**Available endpoints**

The following endpoints are available now.

**/products/**
Returns the first 10 objects ordered with the cheapest first.
 
**/products/kids/**
Returns the products where kids=1 ordered with the cheapest first

**/products/?page=2** 
Returns correspondent page of products. Each page has 10 items.   

**/products/id/**
Returns the individual product.
