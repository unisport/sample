from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Form for creating Products"""

    class Meta:
        model = Product
        fields = "__all__"

