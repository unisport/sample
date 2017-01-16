from django.contrib import admin
from products.models import Item
   
class ItemAdmin(admin.ModelAdmin):
    """
    Class for creating new products in the admin interface. 
    """
    # fields display on change list
    list_display = ['name', 'sizes', 'price']
    # fields to filter the change list with
    list_filter = ['name']
    # fields to search in change list
    search_fields = ['name']
    # enable the date drill down on change list
    date_hierarchy = None
    # enable the save buttons on top on change form
    save_on_top = True
    prepopulated_fields = {}
    # ordering 
    ordering = ['price']

# Register your models here.
admin.site.register(Item,ItemAdmin)
