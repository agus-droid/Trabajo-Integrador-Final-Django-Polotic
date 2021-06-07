from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

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