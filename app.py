from flask import Flask
from flask import render_template
from flask_peewee.utils import object_list
from urllib2 import urlopen
import json
from models import *


app = Flask(__name__)


@app.route('/products/')
#Parsing data from url
def update_db():
    url = 'http://www.unisport.dk/api/sample/'
    request = urlopen(url)
    response = request.read()
    j = json.loads(response)        #Parsing all data from response
    data_list = j['latest']         #Getting list of dicts
#Updating our database
    query = Products.delete()
    query.execute()
    for item in data_list:
        product = Products()
        product.kids = item['kids']
        product.name = item['name']
        product.sizes = item['sizes']
        product.k_adalt = item['kid_adult']
        product.free_porto = item['free_porto']
        product.price = item['price'].replace(',','.')
        product.package = item['package']
        product.delivery = item['delivery']
        product.url = item['url']
        product.price_old = item['price_old'].replace(',','.')
        product.img_url = item['img_url']
        product.product_id = item['id']
        product.women = item['women']
        product.save()    
#After our database was successfully updated we 
#return results paginated by 10 products per page
    return object_list('products.html', Products.select(), paginate_by=10)

#Individual product page
@app.route('/products/<int:id>')
def ind_product(id):
    pr = Products.select().where(Products.product_id == id).get()
    return render_template('ind_product_page.html', 
                            pr=pr, 
                            title='Product id page')

#Products page sorted by price where kids value = 1
@app.route('/products/kids')
def ordered_by_price():
    query = Products.select().where(Products.kids == 1).order_by(Products.price)
    return render_template('cheapest_for_kids.html',
                           query = query,
                           title='The cheapest for kids')


if __name__ == '__main__':
    app.run(debug=False)
