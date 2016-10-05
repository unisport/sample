import web
import requests
import json
from operator import itemgetter

urls = ('/products/', 'list_products', 
        '/products/(.*)/', 'get_product',
        '/products/kids/', 'product_kids')

app = web.application(urls, globals())


class list_products:
    def GET(self, **kwargs):
        source = web.input(page=None)
        products_count = int(source.page) * 10 if source.page else 10
        start = products_count - 10
        resp = requests.get('https://www.unisport.dk/api/sample/')
        data = json.loads(resp.content)
        content = sorted(data['products'][start:products_count],
                         key=itemgetter('price'))
        return content


class product_kids:
    def GET(self):
        resp = requests.get('https://www.unisport.dk/api/sample/')
        data = json.loads(resp.content)
        content = []
        for p in data['products']:
            if p['kids'] == '1':
                content.append(p)
        content = sorted(content, key=itemgetter('price'))
        return content


class get_product:
    def GET(self, p_id):
        resp = requests.get('https://www.unisport.dk/api/sample/')
        data = json.loads(resp.content)
        for p in data['products']:
            if p['id'] == p_id:
                return str(p)


if __name__ == "__main__":
    app.run()