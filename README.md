_Documentation for test task on https://github.com/unisport/sample_

"Write a simple python webservice that uses, manipuates and returns the data found here: [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/)."

Service was written on Django 1.8. In requirements.txt there are additional libraries needed for properly service functionality 

Service has a little bit different data structure like in the semple. It is because I decided to put product sizes into separete model
and use Many_To_One models relation

For frontend I used bootstrap with CDN

To run tests please use commands

../unisport/src$ python manage.py test_coverage products
HTML test_coverege report is in /unisport/test_coverage_report/

To run selenium tests please use commands

../unisport/selenium_tests$ python test_suite.py
Be shure that web-server is running



