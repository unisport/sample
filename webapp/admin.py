from django.contrib import admin
from webapp.models import *

#denne klasse bestemmer hvilke felter der skal vises i admin panelet
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',
    				'kids', 
					'name',
					'sizes',
					'kid_adult',
					'free_porto',
					'price',
					'package',
					'url',
					'price_old',
					'img_url',
					'productID',
					'women'
					)
    search_field = ()

admin.site.register(Product, ProductAdmin)