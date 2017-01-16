from django.contrib import admin
from .models import Product, Size


class ProductAdmin(admin.ModelAdmin):
    pass


class SizeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Size, SizeAdmin)
