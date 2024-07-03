from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    descripcion = forms.CharField(max_length=200, label="Descripcion")
    price = forms.DecimalField(max_digits=10,decimal_places=2, label="precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Disponible", required=False)
    
    def save(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            descripcion = self.cleaned_data['descripcion'],
            price = self.cleaned_data['price'],
            available = self.cleaned_data['available'],
            photo = self.cleaned_data['photo'],
        )