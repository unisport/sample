#!/bin/bash

# Override default template to Unisportize it.
rm /usr/local/lib/python3.6/site-packages/rest_framework/templates/rest_framework/api.html
cp products/templates/rest_framework/api.html /usr/local/lib/python3.6/site-packages/rest_framework/templates/rest_framework/

#Prepare database and get it up to date.
python3 manage.py makemigrations
python3 manage.py migrate

#Populate database with the info found at https://www.unisport.dk/api/sample/
python3 manage.py populatedb

#Start development webserver at port 8000
python3 manage.py runserver 0.0.0.0:8000 
