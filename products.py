import cherrypy
import formencode
from formencode import validators
from config import *


class Product:
    exposed = True


    def validate_data(self, **kw):
        """Creates a validated data dictionary by taking data posted by user
        """
        data = {}
        if kw.get('kids'):
            data.update({'kids': validators.Int().to_python(kw.get('kids', 0))})
        if kw.get('name'):
            data.update({'name': validators.String().to_python(kw.get('name', ''))})
        if kw.get('sizes'):
            data.update({'sizes': validators.String().to_python(kw.get('sizes', ''))})
        if kw.get('url'):
            data.update({'url': validators.String().to_python(kw.get('url', ''))})
        if kw.get('free_porto'):
            data.update({'free_porto': validators.Int().to_python(kw.get('free_porto', 0))})
        if kw.get('price'):
            data.update({'price': validators.Number().to_python(locale.atof(kw.get('price', '0,00')))})
        if kw.get('package'):
            data.update({'package': validators.Int().to_python(kw.get('package', 0))})
        if kw.get('delivery'):
            data.update({'delivery': validators.String().to_python(kw.get('delivery', ''))})
        if kw.get('kid_adult'):
            data.update({'kid_adult': validators.Int().to_python(kw.get('kid_adult', 0))})
        if kw.get('price_old'):
            data.update({'price_old': validators.Number().to_python(locale.atof(kw.get('price_old', '0,00')))})
        if kw.get('image_url'):
            data.update({'image_url': validators.String().to_python(kw.get('image_url', ''))})
        if kw.get('id'):
            data.update({'id': validators.String().to_python(kw.get('id'))})
        if kw.get('women'):
            data.update({'women': validators.Int().to_python(kw.get('women', 0))})
        return data

    def get_products(self, page, kids=False):
        """Returns data based on pagination value and query parameters
        """
        page = int(page)
        offset = (page - 1) * PRODUCTS_PER_PAGE
        limit = page * PRODUCTS_PER_PAGE

        print offset, limit
        if kids:
            items = products.find({"kids": "1"}).sort('price', pymongo.ASCENDING)[offset:limit]
        else:
            items = products.find().sort('price', pymongo.ASCENDING)[offset:limit]

        #items = sorted(_products, key=lambda k: locale.atof(k.get('price', '0')))[offset:limit]
        #output_str = 'ID\tName\tPrice\tKids\n\r'
        style_sheet_str = """<style type="text/css">\
                            table{border-collapse:collapse;}table,th,td {border: 1px solid black;}</style>"""
        output_html = style_sheet_str + """<div><h2>List pf Products</h2></div>\
                    <div><table><tr><td>ID</td><td>Name</td><td>Price</td><td>Kids</td></tr>"""
        for item in items:
            output_html += """<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>""".format(item.get('id'), item.get('name'),
                                                                                                  locale.currency(float(str(item.get('price')))), item.get('kids'))
            #output_str += '{0}\t{1}\t{2}\t{3}\r\n'.format(item.get('id'), item.get('name'),
            # locale.currency(float(str(item.get('price')))), item.get('kids'))
        output_html += '</table></div>'
        return output_html


    def GET(self, *vpath, **params):
        """
        
        """
        if len(vpath) == 0:
            page = params.get('page', 1)
            return '{0}'.format(self.get_products(page))
        else:
            if str(vpath[0]).lower() == 'kids':
                page = params.get('page', 1)
                return '{0}'.format(self.get_products(page, kids=True))
            else:
                _id = vpath[0] if vpath[0].isdigit() else None
                if _id:
                    item = products.find_one({'id': _id})
                    if item:
                        item.pop('_id')
                        output_html = """<div><h3>Here is the product details</h3></div><div><table>"""
                        for k, v in item.iteritems():
                            output_html += """<tr><td><b>{0}</b></td><td>{1}</td></tr>""".format(k.capitalize(), v)
                        output_html += """</table></div>"""
                        return output_html
                    else:
                        return 'No product was found with ID {0}.'.format(_id)


    def POST(self, **kwargs):
        data = self.validate_data(**kwargs)
        _id = products.insert(data)
        return 'A new product with ID {0} has been created'.format(_id)


    def PUT(self, id, **kwargs):
        try:
            product = products.find_one({'id': str(id)})
            if product:
                data = self.validate_data(**kwargs)
                products.update({'_id': product['_id']}, {'$set': data})
                return 'Product with ID {0} has been updated. Here is the updated details {1}'.format(id, product.pop('_id'))
            else:
                return 'No product with the ID {0} found'.format(id)
        except exception, e:
            print e


    def DELETE(self, id):
        product = products.find_one({'id': str(id)})
        if product:
            products.remove({'id': str(id)})
            return 'Product with ID {0} has been deleted'.format(id)
        else:
            return 'No product with the ID {0} was found'.format(id)


if __name__ == '__main__':
    cherrypy.tree.mount(
        Product(),
        '/products',
        {
            '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()