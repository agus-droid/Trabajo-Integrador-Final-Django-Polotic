from django import forms
#from django.contrib.auth.models import User
from users.models import User
from products.models import Product
from categories.models import Category

class RegisterForm(forms.Form):
    username =  forms.CharField(label='Nombre de Usuario',required=True, min_length=4, max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control', 'id':'username'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control', 'id':'email', 'placeholder':'email@ejemplo.com' 
    }))
    password = forms.CharField(label='Contraseña',required=True, min_length=4, max_length=50,widget=forms.PasswordInput(attrs={
        'class':'form-control', 'id':'password'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El nombre de usuario se encuentra en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email se encuentra en uso')
        return email