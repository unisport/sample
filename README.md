UniSample
=========

Simple python webservice that returns the objects & manipuates the data found here [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).


Setup guide
-----------

1. Init python virtualenv:

   Install pillow dependencies:

   - OS X   `$ brew install libjpeg libpng libtiff webp freetype little-cms2 openjpeg`
   - Ubuntu `$ ...`
    
   Install Fabric (command-line tool for systems administration tasks):
    
   `$ pip install fabric`
   
   Init environment:

   `$ fab init_virtualenv`

2. Copy sample file contains settings for this intallation and fill it:

    `$ cp conf/settings/local.py.sample conf/settings/local.py`

3. Activate virtualenv:

    `$ . var/virtualenv/UniSample/bin/activate`

4. Init database:

    `$ python manage.py migrate`

    `$ python scripts/import_external_data.py`

5. Run site:

    `$ python manage.py runserver`
