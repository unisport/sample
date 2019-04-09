Unisport_sample
Unisport coding challenge

Solution to the challenge is made with Flask.

The API data was updated/changed a few days back so I decided to store the data locally in a Db.
/products/

should return the first 10 objects ordered with the cheapest first.

/products/kids/

should return the products where kids=1 ordered with the cheapest first

As of 08-04-2019 no products in the API have the keys "kids" or "kid_adult" 
which is why a complete solution to the /product/kids/ requirement is missing.

/products/?page=2

The products should be paginated where page in the url above should return the next 10 objects

/products/id/

should return the individual product.

Remember to test Remember to document (why, not how)

Bonus: extend the service so the products can also be created, edited and deleted in a backend of choice.

Bonus functionalities added
You are welcome to use any thirdparty python web framework or library that you are familiar with.
