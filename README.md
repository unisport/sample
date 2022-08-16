This rest api is developed using Python and Django with the Django REST framework. 
All of the objectives has been completed, also the CRUD.  


**/Guide to installing dependencies, setting up database, importing data starting server/**

´´´
pip install -r requirements.txt
´´´

´´´
python manage.py makemigrations
´´´

´´´
python manage.py migrate
´´´

´´´
python manage.py importer
´´´

´´´
python manage.py runserver
´´´


**/products/**  


Returns the first 10 objects ordered with the cheapest first.

**/products/?page=2**
 
 The products are paginated where **page** in the url above returns the next 10 objects  

 **/products/id/**
 
returns the individual product.



