**How to setup**

1. setup your database, I used sqlite for this
2. run migrate() from the models file
3. run the populate, it's reading a flat file version of the sample.json data
4. run the tests

**Tests run**

* Say Hello to the Kitty ... ok
* Test first item in the list has to be cheaper ... ok
* Test products for kids sorted by cheapest first ... ok
* Test paginating products is working ... ok
* Test that we get product data by product id ... ok
