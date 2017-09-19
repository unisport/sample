"""
main.py - Unisport Sample webservice

The general layout and semantic of the application is generalized where I thought possible,
    and put into context of each endpoint.
This is done to further the understanding of the process the data goes through,
    which is very much the same at each endpoint.

The endpoints are:
/products
/products/kids
/products/<id>

The endpoints /products and /products/kids also have the ability the take in a page query-parameter,
    which will return the requested page, if it exists, e.g: /products?page=2
All the endpoints will 404, if any query or request is validated falsy.
This is done because I believe standard 404 errors should be a part of a standard API design.

I believe the specific requirements of the web service have been met.
The original repo and said requirements can be found here: https://github.com/unisport/sample
"""

from flask import Flask, jsonify, request, abort
# from requests import get # Easy-to-use function. No hassle with it. Would be used, if data was gotten dynamically

from utilities import paginate, parse_money # Self-made utility functions

app = Flask(__name__)

@app.route("/products")
def products():
    """
    The /products endpoint. The is made as per the design request.
    """

    # Query-parameter as per the design request of the web service api
    selected_page = request.args.get("page")
    products_list = data["products"]
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"]))
    pages = paginate(sorted_products, 10)

    # I didn't a user of the web service to have to specify a page number,
    # if he/she only wants the first page.
    if selected_page is None:
        cheapest_products = pages[0]
    else:
        # Throw a 404, if page doesn't exist. This is done as per the design request.
        if int(selected_page) > len(pages):
            abort(404)
        # Return the queried page.
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/kids")
def kids_products():
    """
    The /products/kids endpoint. The is made as per the design request.
    Will 404, if queried page doesn't exist.
    """

    # Accept a page query-parameter. This done as per the design request.
    selected_page = request.args.get("page")

    # I try to use set builder notation, because it's dense and mathematical.
    products_list = [p for p in data["products"] if p["kids"] == "1"]

    # I used the built-in sorting method because of easy accessibility.
    # It also provides a nice feature for sorting by a specified key.
    sorted_products = sorted(products_list, key=lambda p: parse_money(p["price"], p["currency"])) 

    pages = paginate(sorted_products, 10)

    if selected_page is None:
        cheapest_products = pages[0]
    else:
        if int(selected_page) > len(pages):
            abort(404)
        cheapest_products = pages[int(selected_page) - 1]
    
    return jsonify(cheapest_products)

@app.route("/products/<id>")
def product_by_id(id):
    """
    The /products/<id> endpoint. This is made as per the design request.
    Will 404, if the requested id is not found.
    """
    products_list = data["products"]
    for p in products_list: # Linearly search the products-list. This is done for simplicity.
        if p["id"] == id:
            return jsonify(p)
    abort(404)

if __name__ == "__main__":
    # Data last updated: 19-09-2017 18:05
    # The data is a constant in this case, because of unit testing.
    # Another way would be to dynamically get the data with
    # requests.get("https://www.unisport.dk/api/sample").json()
    #
    # The data is set at the beginning, because the data is more-or-less static.
    # I find no need to get the data every time a call is made to a route.
    data = {
        "end-point": "/api/sample/",
        "products": [
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Lyngby BK Udebanesokker 2016/17",
                "sizes": "37-39, 40-42, 43-45, 46-48",
                "kid_adult": "1",
                "free_porto": "0",
                "image": "https://thumblr-4.unisport.dk/product/153339/a49c1aad13e9.jpg",
                "package": "0",
                "price": "119,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lyngby-bk-udebanesokker-201617/153339/",
                "online": "1",
                "price_old": "119,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153339_maxi_0.jpg",
                "id": "153339",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Sevilla Udebanetrøje 2017/18",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-5.unisport.dk/product/162990/5057e65db993.jpg",
                "package": "0",
                "price": "599,00",
                "url": "https://www.unisport.dk/fodboldtroejer/sevilla-udebanetrje-201718/162990/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/162990_maxi_0.jpg",
                "id": "162990",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "4-8 dage",
                "kids": "0",
                "name": "Tottenham Plakat",
                "sizes": "One Size",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-1.unisport.dk/product/112510/dcfeadc1fe6e.jpg",
                "package": "0",
                "price": "49,00",
                "url": "https://www.unisport.dk/fodboldtroejer/tottenham-plakat/112510/",
                "online": "1",
                "price_old": "49,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/112510_maxi_0.jpg",
                "id": "112510",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Select Nål Protection - Sort",
                "sizes": "One Size",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-8.unisport.dk/product/157755/8900b1658d61.jpg",
                "package": "0",
                "price": "9,00",
                "url": "https://www.unisport.dk/fodboldudstyr/select-nal-protection-sort/157755/",
                "online": "1",
                "price_old": "9,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/157755_maxi_0.jpg",
                "id": "157755",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Werder Bremen NSW Modern Authentic Polo - Grøn/Sort",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-9.unisport.dk/product/164112/cc97b3e0a487.jpg",
                "package": "0",
                "price": "359,00",
                "url": "https://www.unisport.dk/fodboldtroejer/werder-bremen-nsw-modern-authentic-polo-grnsort/164112/",
                "online": "1",
                "price_old": "399,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/164112_maxi_0.jpg",
                "id": "164112",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Lyon Udebaneshorts 2017/18 Børn",
                "sizes": "128 cm, 140 cm, 152 cm, 164 cm, 176 cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-0.unisport.dk/product/161439/f0930fdcda2d.jpg",
                "package": "0",
                "price": "269,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lyon-udebaneshorts-201718-brn/161439/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/161439_maxi_0.jpg",
                "id": "161439",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Chelsea Sutteflaske",
                "sizes": "One Size",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-1.unisport.dk/product/155823/db1499b2e8b0.jpg",
                "package": "0",
                "price": "35,00",
                "url": "https://www.unisport.dk/fodboldtroejer/chelsea-sutteflaske/155823/",
                "online": "1",
                "price_old": "59,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/155823_maxi_0.jpg",
                "id": "155823",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Fortuna Düsseldorf Hjemmebanetrøje 2016/17 Børn",
                "sizes": "YL/152 cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-7.unisport.dk/product/153344/7439bfeef274.jpg",
                "package": "0",
                "price": "137,00",
                "url": "https://www.unisport.dk/fodboldtroejer/fortuna-dusseldorf-hjemmebanetrje-201617-brn/153344/",
                "online": "1",
                "price_old": "549,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153344_maxi_0.jpg",
                "id": "153344",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Nike NSW Tech Fleece Bomber Jakke - Grå/Sort Børn",
                "sizes": "Boys S: 128-137 cm, Boys M: 137-147 cm, Boys L: 147-158 cm, Boys XL: 158-170 cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-8.unisport.dk/product/164019/d8e89d906372.jpg",
                "package": "0",
                "price": "629,00",
                "url": "https://www.unisport.dk/fodbold365/nike-nsw-tech-fleece-bomber-jakke-grasort-brn/164019/",
                "online": "1",
                "price_old": "699,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/164019_maxi_0.jpg",
                "id": "164019",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Wolfsburg Hjemmebaneshorts 2017/18",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-2.unisport.dk/product/164087/222941533da4.jpg",
                "package": "0",
                "price": "299,00",
                "url": "https://www.unisport.dk/fodboldtroejer/wolfsburg-hjemmebaneshorts-201718/164087/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/164087_maxi_0.jpg",
                "id": "164087",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Lazio Hjemmebanetrøje 2017/18 Børn",
                "sizes": "133-145cm/2XS, 146-158cm/X-Small, 159-171cm/Small",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-2.unisport.dk/product/163079/274b065cffdd.jpg",
                "package": "0",
                "price": "519,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lazio-hjemmebanetrje-201718-brn/163079/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163079_maxi_0.jpg",
                "id": "163079",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Inter NSW Modern Authentic Polo - Blå/Sort/Hvid",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-3.unisport.dk/product/163969/3d5d7ce2fa1a.jpg",
                "package": "0",
                "price": "359,00",
                "url": "https://www.unisport.dk/fodboldtroejer/inter-nsw-modern-authentic-polo-blasorthvid/163969/",
                "online": "1",
                "price_old": "399,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163969_maxi_0.jpg",
                "id": "163969",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Lazio 3. Trøje 2017/18",
                "sizes": "Small, Large, X-Large, 3XL, 4XL",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-7.uniid.it/product/163081/7bf2ddba3b89.jpg",
                "package": "0",
                "price": "649,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lazio-3-trje-201718/163081/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163081_maxi_0.jpg",
                "id": "163081",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Lejerbo BK - Baselayer L/Æ Hvid",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-8.unisport.dk/product/153150/ebb844871ed0.jpg",
                "package": "0",
                "price": "279,00",
                "url": "https://www.unisport.dk/team-sport/lejerbo-bk-baselayer-l-hvid/153150/",
                "online": "1",
                "price_old": "279,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/153150_maxi_0.jpg",
                "id": "153150",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "1",
                "name": "Lyon Hjemmebanesæt 2017/18 Mini-Kit Børn",
                "sizes": "92cm, 98cm, 104cm, 110cm, 116cm",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-1.unisport.dk/product/161437/1379174ec063.jpg",
                "package": "0",
                "price": "499,00",
                "url": "https://www.unisport.dk/fodboldtroejer/lyon-hjemmebanest-201718-mini-kit-brn/161437/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/161437_maxi_0.jpg",
                "id": "161437",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Lyngby BK Hjemmebanesæt Årgang 2006 Drenge",
                "sizes": "",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-8.unisport.dk/product/92025/81ab22a22d8a.jpg",
                "package": "1",
                "price": "575,00",
                "url": "https://www.unisport.dk/team-sport/lyngby-bk-hjemmebanest-argang-2006-drenge/92025/",
                "online": "1",
                "price_old": "687,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/92025_maxi_0.jpg",
                "id": "92025",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Crystal Palace Hjemmebanetrøje 2017/18",
                "sizes": "Small, Medium, Large, X-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-7.unisport.dk/product/163090/7691c0743bb0.jpg",
                "package": "0",
                "price": "629,00",
                "url": "https://www.unisport.dk/fodboldtroejer/crystal-palace-hjemmebanetrje-201718/163090/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163090_maxi_0.jpg",
                "id": "163090",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Bologna Udebanetrøje 2017/18",
                "sizes": "Small, Medium, Large, X-Large, XX-Large, 3XL",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-2.uniid.it/product/163083/2ece2f326e34.jpg",
                "package": "0",
                "price": "599,00",
                "url": "https://www.unisport.dk/fodboldtroejer/bologna-udebanetrje-201718/163083/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163083_maxi_0.jpg",
                "id": "163083",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Deportivo De La Coruña Hjemmebanetrøje 2017/18",
                "sizes": "Small, Medium, Large, X-Large, XX-Large, 3XL",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-6.unisport.dk/product/163103/cdff6f7a33ca.jpg",
                "package": "0",
                "price": "629,00",
                "url": "https://www.unisport.dk/fodboldtroejer/deportivo-de-la-coruna-hjemmebanetrje-201718/163103/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163103_maxi_0.jpg",
                "id": "163103",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Nice Polo - Sort",
                "sizes": "Small, Medium, Large, X-Large, XX-Large, 3XL",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-7.unisport.dk/product/163098/7e5e2ed5d5af.jpg",
                "package": "0",
                "price": "445,00",
                "url": "https://www.unisport.dk/fodboldtroejer/nice-polo-sort/163098/",
                "online": "1",
                "price_old": "445,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163098_maxi_0.jpg",
                "id": "163098",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Sporting Lissabon 3. Trøje 2015/16",
                "sizes": "Small, Medium, Large, X-Large, XX-Large, XXX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-4.unisport.dk/product/163101/4e6eb5261ea5.jpg",
                "package": "0",
                "price": "649,00",
                "url": "https://www.unisport.dk/fodboldtroejer/sporting-lissabon-3-trje-201516/163101/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163101_maxi_0.jpg",
                "id": "163101",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Nice Træningsbukser - Sort",
                "sizes": "Small, Medium, Large, X-Large, XX-Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-9.unisport.dk/product/163097/ec933394bc81.jpg",
                "package": "0",
                "price": "349,00",
                "url": "https://www.unisport.dk/fodboldtroejer/nice-trningsbukser-sort/163097/",
                "online": "1",
                "price_old": "389,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163097_maxi_0.jpg",
                "id": "163097",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Nice 3. Trøje 2017/18",
                "sizes": "Small, Large",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-6.unisport.dk/product/163095/da6d588c5a09.jpg",
                "package": "0",
                "price": "669,00",
                "url": "https://www.unisport.dk/fodboldtroejer/nice-3-trje-201718/163095/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163095_maxi_0.jpg",
                "id": "163095",
                "women": "0"
            },
            {
                "is_customizable": "0",
                "delivery": "4-8 dage",
                "kids": "0",
                "name": "Leeds United Blade Puttercover + Markør",
                "sizes": "One Size",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-2.unisport.dk/product/134179/252672733f41.jpg",
                "package": "0",
                "price": "189,00",
                "url": "https://www.unisport.dk/fodboldtroejer/leeds-united-blade-puttercover-markr/134179/",
                "online": "1",
                "price_old": "189,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/134179_maxi_0.jpg",
                "id": "134179",
                "women": "0"
            },
            {
                "is_customizable": "1",
                "delivery": "1-2 dage",
                "kids": "0",
                "name": "Hajduk Split 3. Trøje 2017/18",
                "sizes": "Small",
                "kid_adult": "0",
                "free_porto": "0",
                "image": "https://thumblr-8.uniid.it/product/163128/8ababd142bd2.jpg",
                "package": "0",
                "price": "549,00",
                "url": "https://www.unisport.dk/fodboldtroejer/hajduk-split-3-trje-201718/163128/",
                "online": "1",
                "price_old": "0,00",
                "currency": "DKK",
                "img_url": "https://s3-eu-west-1.amazonaws.com/product-img/163128_maxi_0.jpg",
                "id": "163128",
                "women": "0"
            }
        ]
    }
    app.run(debug=True)
