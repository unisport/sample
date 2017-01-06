from django.contrib import admin

from products.models import Product, Size, SourceSettings


admin.site.register(Product)
admin.site.register(Size)
admin.site.register(SourceSettings)

