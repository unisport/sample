from django.contrib import admin
from api.models import Product

@admin.register(Product)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price')
