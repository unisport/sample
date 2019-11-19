Here's my submit to the coding challenge.

The project is done in Django and also uses a few other packages.
`pip install -r requirements.txt`

Since the API below no longer returns products, I found a way to do it by watching the XHR Network tab in Dev tools.
`get_products_from_api.py` pulls some products from the live site into 3 json files.

I couldn't find a proper way to import the products into the Django DB.. probably something to do with the environment settings. To get around this I made a hacky solutions and imported the products through a "hidden" view called from `127.0.0.1:8000/import`. This should obviously not be left there if going to production :)

I freestyled a bit over the challenge, so my solution includes product lists views for **brands**, **male**, **female** and **kids**.. as well as a **outlet** category with discount > 30%. I also added some Bootstrap styling to make it all look like a proper website. 

I would have liked to have more info on the product details view, but the api doesn't return product description and additional photos. I could probably have scraped it from the site, but since its a javascript rendered frontend, that turned out to be more work, than I anticipated. Long story short.. I faked the product description.

___


_Fork this project and send us a pull request_

Write a simple python webservice that uses, manipuates and returns the data found here: [https://www.unisport.dk/api/products/batch/](https://www.unisport.dk/api/products/batch/?list=179249,179838,174351,180011,180020,178429).


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

#### Bonus:
 extend the service so the products can also be created, edited and deleted in a backend of choice.


_You are welcome to use any thirdparty python web framework or library that you are familiar with._  

#### Forking and Pull Requests
Information on how to work with forks and pull requests can be found here https://help.github.com/categories/collaborating-with-issues-and-pull-requests/
