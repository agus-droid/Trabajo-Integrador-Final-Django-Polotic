from django import forms

class RegisterForm(forms.Form):
    username =  forms.CharField(required=True, min_length=4, widget=forms.TextInput(attrs={
        'class':'form-control', 'id':'username', 'placeholder':'username'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class':'form-control', 'id':'email', 'placeholder':'email' 
    }))
    password = forms.CharField(required=True, min_length=4, widget=forms.PasswordInput(attrs={
        'class':'form-control', 'id':'password'
    }))