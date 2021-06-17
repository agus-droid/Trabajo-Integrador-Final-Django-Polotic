from products.models import Product
from django import forms
from categories.models import Category

class NewProductForm(forms.Form):
    title = forms.CharField(label='Titulo del Producto', required=True, min_length=4, max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control', 'id':'title'
    }))
    description = forms.CharField(label='Descripción',required=True, widget=forms.Textarea(attrs={
        'class':'form-control', 'id':'description'
    }))
    category = forms.ModelChoiceField(label='Categoría', queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={
        'class':'form-control', 'id':'category'
    }))
    price = forms.DecimalField(label='Precio',max_digits=16, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control', 'id':'price'
    }))
    image = forms.ImageField(label='Imagen del Producto', required=True, widget=forms.FileInput(attrs={
        'class':'form-control', 'id':'image', 'name':'image'
    }))