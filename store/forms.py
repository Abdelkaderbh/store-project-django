from django import forms
from .models import Categorie, Fournisseur, Stock


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name', 'description']

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['name', 'contact_info', 'email']
               
class ProductForm (forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
    