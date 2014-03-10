A simple python webservice in Flask that returns the objects & manipuates the data found here [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/). The webservice is tested with Python 3.3.4

####Setup:

1. Create a virtualenv e.g.:

        mkvirtualenv sample

2. Install necessary requirements with pip:

        pip install -r requirements

3. Run tests:

        python tests.py

4. Sync the database:

        python manage.py db init
        python manage.py db upgrade
        python manage.py db migrate
        python manage.py seed

5. Run the server:

        python manage.py runserver


####Usage
1. Returns the 10 cheapest items

        GET
        /products/

2. Return the products where kids=1 ordered with the cheapest first

        GET
        /products/kids/

3. Paginated where **page** in the url returns the next 10 objects  

        GET
        /products/page/2

4. Return the individual product
    
        GET 
        /products/id/
