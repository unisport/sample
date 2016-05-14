from django.contrib import admin

from .models import Product, Size

class SizeInline(admin.StackedInline):
	model = Size

class ProductAdmin(admin.ModelAdmin):
	inlines = [SizeInline]

admin.site.register(Product, ProductAdmin)
# admin.site.register(Size)