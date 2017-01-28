# Unisport Sample Products Application

A simple python webservice that uses, manipulates and returns the data 
found here: [http://www.unisport.dk/api/sample/](http://www.unisport.dk/api/sample/).


## Tests and linting

Tests and `flake8` could be run in separate envs using `tox`. Install
`tox` using the following command:

```console
$ pip install tox
```

### `tox` usage

Run all configured `tox` environments:

```console
$ tox
```

Run only a specific environment:

```console
$ tox -e flake8
$ tox -e test
```

Pass arguments to commands:

```console
$ tox -e flake8 -- unisport_sample/wsgi.py
$ tox -e test -- path.to.test_module:TestCase.test_method
```

## Task requirements

**/products/**  


should return the first 10 objects ordered with the cheapest first.
 
**/products/kids/**
 
should return the products where kids=1 ordered with the cheapest first

**/products/?page=2**
 
 The products should be paginated where **page** in the url above should return the next 10 objects  

 **/products/id/**
 
should return the individual product.


 
**_Remember to test_**   
**_Remember to document (why, not how)_**

####Bonus:
 extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._  

