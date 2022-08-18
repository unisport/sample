from django import forms
from django.contrib import admin
from django.forms.widgets import Textarea

from unisport.unisport_data.models import Currency, Product, Stock


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("id",)

    widgets = {
        "name": Textarea(attrs={"cols": 30, "rows": 1}),
        "delivery": Textarea(attrs={"cols": 30, "rows": 1}),
        "relative_url": Textarea(attrs={"cols": 30, "rows": 1}),
        "url": Textarea(attrs={"cols": 30, "rows": 1}),
    }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ("id",)


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id",)
    form = CurrencyForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "recommended_retail_price", "currency")
    list_per_page = 10
    form = ProductForm


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    form = StockForm
