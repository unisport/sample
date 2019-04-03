Unisport code_challenge

Solution to Unisport_code_challenge

I have choosen to use the Django framework, after a little bit of research it seemed like a good choice for the assignment. As you were able to get a site up and run pretty fast. And the admin part of Django, was a nice feature for the bonus assignment.

Dependencies : - Python 3 (version 3.7.3) - Django 2.1.7 (pip install django)

    Browse to Unisport_code_challenge
    Run: py manage.py runserver 

You can now browse ot : http://localhost:8000/challenge/ - And access my solution.

Tasks:

Write a simple python webservice that uses, manipulates and returns the data found here: http://www.unisport.dk/api/sample/.

As I found out today, you have changed the data on https://www.unisport.dk/api/sample/, I had to rewrite my import function to use a file with the old data. So if you run import_json.py it will take the data an import into the SQLite DB. (Its already done in these files.)

All the task below is setup through Django, via views and html files. (Templates)
The code written to receive data from the DB is written in the views.py file. You can find the HTML files in /templates/challenge/ there is a minimum of code in these files.
The models.py file, have the data structure for the datamodel in Django and the DB.

/products/

should return the first 10 objects ordered with the cheapest first.

/products/kids/

should return the products where kids=1 ordered with the cheapest first

/products/?page=2

The products should be paginated where page in the url above should return the next 10 objects

/products/id/

should return the individual product.

Remember to test Remember to document (why, not how)

As said Django delievers this feature built in, with very little code to open for. You can enter the admin page on http://localhost:8000/admin/ (User:admin/Pass:admin)

Bonus:

extend the service so the products can also be created, edited and deleted in a backend of choice. You are welcome to use any thirdparty python web framework or library that you are familiar with.

Hope you enjoy the solution.
