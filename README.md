# Adapt
### Unisport task

Simple python web service that uses, manipulates and returns the data found here: https://www.unisport.dk/api/products/batch/.

## Installation

```
pip install -r requirements.txt
```

## Usage

```
export FLASK_APP=main.py &&
flask run
```

## Endpoints

#### /products/

By default returns the first 10 products ordered with the cheapest first.
For more objects use the *optional* `items` query parameter.

E.g.:
`/products/?items=<NUMBER_OF_ITEMS>`

#### /products/?page=2

Pagination returns `next_page_id` and 10 products by default, which can also be changed by specifying the number of items in the *optional* `items` query parameter.

E.g.:
`/products/?page=<PAGE_ID>&items=<NUMBER_OF_ITEMS>`

#### /products/id/

Returns individual product.

E.g.:
`/products/id/product=<ID>`

## Tests

I didn't have any time to implement unit or integration tests, which I had initially planned to do.

If you need them for the admission process and you're able to wait a couple of days, ping me, I would be happy to implement them.

## Author
[Pijus Rancevas](https://github.com/pijus-r) | [LinkedIn](https://www.linkedin.com/in/pijus-rancevas/) 


## License
[MIT](https://choosealicense.com/licenses/mit/)