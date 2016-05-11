#coding: utf-8
from django import forms
import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Product
        fields = '__all__'

