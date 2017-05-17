# Sample Documentation
* * * * * * * * * * * * *

## Introduction

The project was quite rushed due to other assignments @University. Because of
this I have written an extra section about 'what i would have done'.

I have chosen not to use a database in this *sample* because it seemed
unnecessary unless I would do the **Bonus** part.

The default installed apps: admin, auth, contenttypes, sessions, messages,
statistics and productsConfig are not used.

## Layout of the project
I've chosen to make the sample as a Django App instead of the root project.
This is because if I was to add more functionality to the site I could simply
add another app and add an `include('new_app_name')` and a regular expression
to map the new app to another url. I wouldn't expect the '/products'-app to be
the main functionality of the site.

Mostly all the configuration is default from Django's
`django-admin startproject`

### templates/ and static/
The one and only *templates/* and *static/* folders i use is inside the
`products` app because I was lazy and didn't thought it would be relevant to
add a special templates and static folder for the root directory of the site.

And it would be a waste of time when i could spend it on more important things
in the project.

## Functions
Description of the choices I've made regarding the functions found in
**products/views.py**

### getJsonDataFromServer()
There isn't much to this function except I use a `try-except` to catch anything
thrown by `urlopen( ... )`

The return of this function is Json-dict format because it's easy to read,
understand and use.

### products\_sorted\_by\_price( items, index, amount )
This function was originally calling `getJsonDataFromServer()` but was changed
to get the items as an arguement because I wanted to use it for the
**products/kids/** section of the assignment too. This way we don't need to
sort EVERYTHING before deciding what to keep and not to keep.

* `items`  is a list of the items to sort.
* `index`  is from where we want the sorted items.
* `amount` is the quantity of items we want in return. We can just count
           `amount` items forward from `index` in our list to get the return
           list.

The `sorted\_items` calls `sorted( ... )` in which we throw a lambda-function.
I used these because it makes the code more readable (I think). In the lambda I
throw the string to a float, because the format is so, and substitude all the
commas with punctuations. If not, the lambda would throw an error.

The `elif` on line **34** checks if the function is able to return the given
quantity. If not, return everything preceding `index`.

### getProductByID( id )
Searches all the products for a given `ID`.
Looking back it would have been way more efficient to just look through a given
list if you could map an estimate index from the list of all products.

Throws 404 if it cannot find the given ID in any of the products.

### IndexView
This is used both for *products/* and for *products/kids*. I have made it the
way that it finds out which it should act like by reading the url from which
it was accessed.

#### get\_page\_number( self, request )
I made it so it would only return a number other than 1 if the arguement in
GET is valid. This way we avoid errors when the user tries to mess with the
system by trying to enter random stuff in the url.

#### get\_queryset( self )
I made it so it runs a check wether or not the product list should only contain
products with the "kids" or "kid\_adult" flag, because the Dumb on
*unisport.com/api/sample* didn't contain anything with the "kids" flag set to
ON.

It fowards the next and previous page number to the template because I didn't
wanted to spend too much time making template tags to subtract or add page
number.

### detail( product\_id, item\_list )
This was originally used for the detailview for all the products, but because I
included navigation in the detail-view I had to rewrite it so it would fit
in the kid-section too.

**Site navigation is explained later.**

I've made it so it would find the previous ID and next ID of the current item
in the `item_list`. This way we can tell the template what to link to in the
navigation bar.

### product\_details and kid\_details( request, product\_id )
These functions are basically wrappers for the `detail` function.

## Site navigation
I thought it would be intuitive to have a navigation bar in the details view
too. So what I made was a navigation bar that - instead of navigation through
pages - navigated through the sorted list represented on the pages.

## Tests
I used unit tests because it is a good way to test small parts of the app to
see if everything works and behaves as expected.

The tests are a disaster. I got quite discouraged when the first test I wrote
would't work because of my implementation of the sorting function. even though
the test is just a lazy way of counting the returned elements from
`products_sorted_by_price( ... )`.
The smoketest is to make sure the `getJsonDataFromServer` doesn't throw any
exceptions.
The test on the detailsview is to make sure that it returns the proper HTTP
status codes.

## A better implementation
If I was given more time to do this I would have made a local database, and a
button which would update the local from *unisport.com/api/sample*, such that
it would not depend on another server.

If I was given a bigger dataset I would have presorted the data by price
(problematic if we should let the user choose how to sort it). The algorithm I
would use would be bubblesort, whenever a new product got added to the list
(since it's best case is **N** (considering a list of the size **N**) when used
on a nearly sorted list). For first-time sorting I would use mergesort, since
it has a very stable sorting time on random sorted lists.
To find a specific product would be easy since I would try to find the specific
product by a "divide-and-conquor" method, which has the runtime of

    O(n) = log2( n ) * n

I would also have used a custom model, but hardcoding one matching the data
from *unisport.com/api/sample* would have been too time-consuming. The model
would of course have been used in a generic `DetailView class`.

* * * * *

*This concludes my solution to your sample-assignment/test*

Regards, Oscar
