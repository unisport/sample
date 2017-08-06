_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).

Uni Sport Product assignment
======================

Requirements
------------
Django==1.10.6

Python3.4.3


Setup
----------
**Python Environment**

1. Install pip: apt-get -y install python-pip

2. Install and configure virtualenv using Python 3.4 (/usr/lib/python3.4): virtualenv -p PYTHON3.4_DIR u YOUR_ENV_NAME - http://docs.python-guide.org/en/latest/dev/virtualenvs/

3. source virtualenv/bin/activate

4. Install the packages from requirements.txt: pip install -r requirements.txt


Tests
------ 
1. cd to sample/unisport

2. type into terminal: export DJANGO_SETTINGS_MODULE=unisport.settings

3. To run test type: python -m unittest tests.ViewsTestCase

Comments
---------

As seen in the code I dont use a database. no model object is used in the model.py. The reason behind that is that it was not required and I wanted to keep the code simple. 

**####Bonus: extend the service so the products can also be created, edited and deleted in a backend of choice.**

Django provide an admin, in which you can use to delete, create annd delete in a backend of choice. 


