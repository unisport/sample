import lxml
import lxml.html

from model.product import Product


def add_product(db, **kwargs):
    default_product = {}
    default_product.update(**kwargs)
    db.session.add(Product(**default_product))
    db.session.commit()


def retrieve_products(html_string):
    data = []
    html = lxml.html.document_fromstring(html_string)
    headers = [header.text for header in html.xpath('//table[@id="products"]//th')]
    rows = html.xpath('//table[@id="products"]//tr')[1:]
    for row in rows:
        columns = row.xpath('td')
        prod_id = int(columns[0].xpath('a')[0].text)
        parsed_columns = [column.text for column in columns[1:]]
        data.append(dict(zip(headers, [prod_id] + parsed_columns)))
    return data


def retrieve_product(html_string):
    data = {}
    html = lxml.html.document_fromstring(html_string)
    input_elements = html.xpath('//input')
    for input_element in input_elements:
        name = input_element.xpath('@name')[0]
        value = input_element.xpath('@value')[0]
        if name == 'id':
            data.update({name: int(value)})
        else:
            data.update({name: value})
    return data
