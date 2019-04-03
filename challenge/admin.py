from django.contrib import admin

# Making the App visible and usable through the admin module

from .models import Product

admin.site.register(Product)
