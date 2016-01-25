Copy the script to a local machine.
Make sure that there is python in the Path environment variables (it should be installed separately).
Launch the run_django_server.bat for testing the app with the django debug web server.
Go to the http://127.0.0.1:8000/products/ in a web browser.
Use product id from the startpage to check the 4 task - /products/id/. For example http://127.0.0.1:8000/products/35607/
Launch the run_tests.bat for unit tests. NOTE: the "mock" should be installed separately

NOTE: set the settings.DEBUG = False before using on a production )