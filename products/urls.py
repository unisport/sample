from django.conf.urls import patterns, include, url

urlpatterns = patterns('products.views',
    (r'^products-list/$', 'products_list'),
    (r'^products-list/(?P<page>[\d]*?)/$', 'products_list'),
    (r'^products-list/(?P<page>[\d]*?)/(?P<items>[\d]*?)/$', 'products_list'),
    (r'^edit-product/$', 'edit_product'),
    (r'^edit-product/(?P<product_id>[\d]*?)/$', 'edit_product'),
    (r'^delete-product/(?P<product_id>[\d]*?)/$', 'delete_product'),

    (r'^sizes-list/$', 'sizes_list'),
    (r'^sizes-list/(?P<page>[\d]*?)/$', 'sizes_list'),
    (r'^sizes-list/(?P<page>[\d]*?)/(?P<items>[\d]*?)/$', 'sizes_list'),

    (r'^edit-size/$', 'edit_size'),
    (r'^edit-size/(?P<size_id>[\d]*?)/$', 'edit_size'),
    (r'^delete-size/(?P<size_id>[\d]*?)/$', 'delete_size'),

    (r'^(?P<product_id>[\d]*?)/$', 'view_product'),
    (r'^$', 'main_page'),
    (r'^(?P<category>[\w\/\-]+)/$', 'main_page'),
)
