### Endpoints

**/products/**

This endpoint returns the first 10 objects ordered with the cheapest first.<br>
A POST request with all relevant product fields will create a new product.

**/products/kids/**

This endpoint returns the products where the age group is set as "Kids" ordered with the cheapest first. This is also paginated.

**/products/?page=2**

Returns products 10 through 20, because page size is set to 10. Ordered by cheapest.

**/products/\<int:id>/**

A GET request returns the individual product.<br>
A PUT request with all relevant product fields will update the product.<br>
A DELETE request will remove the product.

### Bonus

I created a very primitive frontend that can view the products in store and create new products

### Set up

- Clone repo
- `python -m venv env` and activate the environment.
- `pip install -r requirements.txt`
- `python manage.py collectstatic`
- `python manage.py migrate`
- `python manage.py resetdb`. This command is provided by me, it fetches about 25 products from the API and stores them in the database.
- `python manage.py runserver`
