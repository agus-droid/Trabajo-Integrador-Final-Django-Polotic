from django.shortcuts import render
from .utils import get_or_create_cart
# Create your views here.

def cart(request):   
    get_or_create_cart(request)
    return render(request, 'carts/cart.html',{

    })