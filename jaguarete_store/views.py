from categories.models import Category
from django.http.response import HttpResponseRedirect
from products.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from users.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import user_passes_test

def index(request):
    products = Product.objects.all().order_by('-id')
    print('hola')
    return render(request,'index.html',{
        'products': products
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')   
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}.'.format(username))
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('index')
        else:
            messages.error(request, 'Usuario y/o contraseña invalido/s')

    return render(request, 'users/login.html', {
        'title': 'Iniciar sesión'
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'La sesión se cerró exitosamente')
    return redirect('login')

def register(request):
    if request.user.is_authenticated:
        return redirect('index')    
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
        'form': form,
        'title': 'Registro'
    })

def about(request):
    return render(request, 'about.html',{
        'title': 'Acerca de...'
    })

