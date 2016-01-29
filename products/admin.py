from django.contrib import admin

# Register your models here.

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['id',
                'name',
                'sizes',
                'delivery',
                'price',
                'price_old',
                'url',
                'img_url',
                'kids',
                'women',
                'kid_adult',
                'free_porto',
                'package',
    ]


admin.site.register(Product)