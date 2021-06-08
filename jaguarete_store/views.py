from jaguarete_store.forms import RegisterForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm

def index(request):
    return render(request,'index.html',{
        'message':'Listado de productos',
        'title':'Productos',
        'products':[
            {'title': 'Milanesas', 'price':'800', 'stock':True},
            {'title': 'Papas Fritas', 'price':'120', 'stock':True},
            {'title': 'Lamborghini Aventador LP700-4', 'price':'8000000', 'stock':False},
        ]
    })

def login_view(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}.'.format(username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario y/o contraseña invalido/s')

    return render(request, 'users/login.html', {

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'La sesión se cerró exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado')
            return redirect('index')
    return render(request, 'users/register.html',{
        'form': form
    })