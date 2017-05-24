**Introduction**

Entry submission for the Unisport Code Challenge.

Make automation tool was used for tasks like:

* Setting up project environment dependencies
* Migrating data from Unisport sample api to a locale sqlite database
* Unit testing
* Validation of source code
* Code coverage

**How to setup**

To make sure that the necessary dependencies are installed:

    make setup


**Running the Unit Tests**

    make test

**Running the web service**

First run `` make migrate `` to generate and populate a database with data:

    make migrate

To run a locale instance of the web service:

    make run
