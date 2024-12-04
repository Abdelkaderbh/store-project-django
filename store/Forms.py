from django.forms import ModelForm
from store.models import Stock

class ProductForm (ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'