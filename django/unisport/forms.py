from django import forms

from unisport import models


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Add the form-control class to each TextInput field so that
        # they are styled using bootstrap.
        for name, field in self.fields.iteritems():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': 'form-control'
                })

    class Meta:
        model = models.Product
