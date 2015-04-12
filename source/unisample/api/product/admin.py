from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
