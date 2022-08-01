## Unisport Sample - Guidelines to run project

### In an activated virtual env run the following commands
**Install dependencies**
```
pip install --upgrade pip
pip install -r requirements.txt
```
**Set up database and add data**
```
python manage.py makemigrations
python manage.py migrate
python manage.py provision
python manage.py add_unisport_data
```
**Start server**
```
python manage.py runserver
```

**Most important files**
- unisport_app/views.py
- unisport_app/models.py
- unisport_app/tests.py
- unisport_app/templates/unisport_app/*

**Access backend**
- Run provision script
- Start server
- Go to: ['http://127.0.0.1:8000/admin/'](http://127.0.0.1:8000/admin/)
**Username:** unisport
**Password:** unisport


_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [https://www.unisport.dk/api/products/batch/](https://www.unisport.dk/api/products/batch/?list=200776,213591,200775,197250,213590,200780,209588,217706,205990,212703,197237,205989,211651,213626,217710,200783,213576,202483,200777,203860,198079,189052,205946,209125,200784,190711,201338,201440,206026,213587,172011,209592,193539,173432,200785,201442,203854,213577,200802,197362).


**/products/**  


should return the first 10 objects ordered with the cheapest first.

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
