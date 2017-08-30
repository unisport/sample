# -*- coding: utf-8 -*-
# try something like

def newform():
    form= SQLFORM(db.products).process()
    return locals()

def view():
    rows= db(db.products).select()
    pricesort = rows.sort(lambda p: (float(p['price'].replace(',', '.'))))
    return locals()

def products():
    response.title += ' | Pruducts'
    if not request.vars.page:
         redirect(URL(vars={'page':1}))
    else:
             page = int(request.vars.page)
    start = (page-1)*10
    end = page*10
    rows= db().select(db.products.ALL,limitby=(start,end))
    pricesort = rows.sort(lambda p: (float(p['price'].replace(',', '.'))))
    return locals()


def kids():
    records = db(db.products.kids==1).select()
    pricesort = records.sort(lambda p: (float(p['price'].replace(',', '.'))))
    return dict(records=pricesort)


def update():
    record = db.products(request.args(0)) or redirect(URL('view'))
    form= SQLFORM(db.products,record)
    if form.process().accepted:
        response.flash= T('Record Updated')
        redirect(URL('view'))
    else:
        response.flash = T('Please fill the form properly')
    return locals()

def delete():
    record = db.products(request.args(0)) or redirect(URL('view'))
    form= SQLFORM(db.products,record,deletable=True)
    if form.process().accepted:
        response.flash= T('Record deleted')
        redirect(URL('view'))
    else:
        response.flash = T('Please select a check box to delete data at the bottom')
    return locals()

def grid_products():
    grid = SQLFORM.grid(db.products,paginate=10,buttons_placement = 'left')
    return locals()

def grid_test():
    """     
    >>> grid = SQLFORM.grid(db.products,paginate=10,buttons_placement = 'left')
    grid = SQLFORM.grid(db.products,paginate=20,buttons_placement = 'left')
   
    """
    return locals()
