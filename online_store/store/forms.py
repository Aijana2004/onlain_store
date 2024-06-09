from django import forms
from .models import Product


class Productforms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','description','price','active','category','date']