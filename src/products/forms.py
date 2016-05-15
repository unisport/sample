from django.forms import ModelForm
from .models import Product

class ProductModelForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__' #not recomend if you have privite fields or will add them in future
