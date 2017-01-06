from django.contrib import admin
from . models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
