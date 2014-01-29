# -*- coding: utf-8 -*-
from django import forms

from models import Product, ProductSize


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("price_old", "deleted", "from_json")


class ProductSizeForm(forms.ModelForm):
    class Meta:
        model = ProductSize