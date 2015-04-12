Project setup guide (for Ubuntu 12.04)
======================================

General requirements
--------------------
Install basic system tools and git for code management

    root# apt-get update
    root# apt-get install sudo mc htop
    root# apt-get install build-essential git

Python
------
Install python and libs required to build several python packages 

    root# apt-get install python2.7 python2.7-dev python-setuptools
    root# easy_install pip
    root# pip install fabric virtualenv supervisor

    root# apt-get install libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
    root# apt-get install libxslt-dev libxslt1-dev libxml2-dev

    root# ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
    root# ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
    root# ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/

nginx
-----
Stop Apache server if running, then install nginx.

_Note: new system user www-data will be created_

    root# /etc/init.d/apache2 stop
    root# apt-get install nginx

Create home dir for www-data user, this will be home for UniSample site.

    root# mkdir /home/sites
    root# chown www-data /home/sites
    root# usermod -d/home/sites www-data
    root# usermod -s/bin/bash www-data

PostgreSQL
----------

Install PostgreSQL and dev libs

    root# apt-get update
    root# apt-get install postgresql-9.1 libpq-dev

Set password to system postgres user

    root# passwd postgres

Create user(role) and database

    root# sudo -u postgres psql
    postgres=# ALTER USER postgres WITH PASSWORD '<SOME_PASSWORD_1>';
    postgres=# CREATE USER projectuser WITH password '<SOME_PASSWORD_2>';
    postgres=# CREATE DATABASE unisample WITH OWNER projectuser;
    postgres=# \q


Create Password File (optional).
Read more at http://www.postgresql.org/docs/9.1/static/libpq-pgpass.html

    root# sudo -u www-data -i
    www-data$ mcedit ~/.pgpass
    > localhost:5432:postgres:*:<SOME_PASSWORD_1>
    > localhost:5432:projectuser:unisample:<SOME_PASSWORD_2>

SSH + BitBbucket
----------------
If you already have ssh key pair just put in '.ssh' dir.

    root# sudo -u www-data -i
    www-data$ mkdir ~/.ssh
    www-data$ mcedit ~/.ssh/id_rsa
    www-data$ mcedit ~/.ssh/id_rsa.pub
    www-data$ chmod 600 /home/sites/.ssh/id_rsa
    www-data$ chmod 600 /home/sites/.ssh/id_rsa.pub

If you don't have then create new pair.

    root# sudo -u www-data -i

    www-data$ ssh-keygen
      > Path: /home/sites/.ssh/id_rsa (Default)
      > Password: No password

Open **public key** in file `/home/sites/.ssh/id_rsa.pub` and copy this key to 
[bitbucket account](https://bitbucket.org/account/projectuser/unisample/ssh-keys/)

Site setup
----------
Get site code, its requirements and start site.

Note: there is a problem if you are using `django-celery==3.0.xx`.
It depends on `pytz`, which is required to be updated each quarter.
To fix problem update version of `django-celery` to newer one.

    root# sudo -u www-data -i

    www-data$ mkdir /home/sites/UniSample
    www-data$ cd /home/sites/UniSample
    www-data$ git clone git@bitbucket.org:projectuser/unisample.git DEMO
    www-data$ cd /home/sites/UniSample/DEMO/conf/settings
    www-data$ cp local.py.sample local.py && mcedit local.py

    www-data$ cd /home/sites/UniSample/DEMO
    www-data$ fab init_virtualenv

    www-data$ fab demo generate_config_files
    www-data$ fab deploy

    www-data$ exit


Add nginx config to file `/etc/nginx/sites-available/unisample`.
Use file `config/nginx_dev.conf` as example.

    root# mv /home/sites/UniSample/DEMO/conf/_nginx_unisample_dev.conf /etc/nginx/sites-available/unisample
    root# rm /etc/nginx/sites-enabled/default
    root# rm /etc/nginx/sites-available/default
    root# ln -s /etc/nginx/sites-available/unisample /etc/nginx/sites-enabled/unisample
    root# /etc/init.d/nginx restart
