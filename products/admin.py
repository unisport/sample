from django.contrib import admin

from models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'sizes')
    list_filter = ('kid_adult', 'kids', 'free_porto', 'women', 'package')
    search_fields = ('name', 'sizes')


admin.site.register(Product, ProductAdmin)
