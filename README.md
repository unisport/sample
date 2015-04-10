Skeleton for django project
===========================

Typical django project structure polished by years.

Setup guide
-----------

1. Init python virtualenv:

    Install pillow dependencies

    - OS X   `$ brew install libjpeg libpng libtiff webp freetype little-cms2 openjpeg`
    - Ubuntu `$ ...`

   `$ fab init_virtualenv`

2. Copy sample file contains settings for this intallation and fill it:

    `$ cp conf/settings/local.py.sample conf/settings/local.py`

3. Activate virtualenv:

    `$ . var/virtualenv/UniSample/bin/activate`

4. Init database:

    `$ python manage.py migrate`

5. Run site:

    `$ python manage.py runserver`
