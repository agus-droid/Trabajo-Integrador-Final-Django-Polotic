import products
from django.shortcuts import get_object_or_404, render, redirect
from .utils import get_or_create_cart
from products.models import Product
from .models import CartProducts
# Create your views here.

def cart(request):   
    cart = get_or_create_cart(request)
    return render(request, 'carts/cart.html',{
        'cart': cart
    })

def add(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    if int(request.POST.get('quantity', 1)) < 1:
        quantity = 1
    else:
        quantity = int(request.POST.get('quantity', 1))
    
    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart,
                                                                    product=product, 
                                                                    quantity=quantity)
    return render(request, 'carts/add.html',{
        'quantity':quantity,
        'product': product,
        'cart_product': cart_product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    cart.products.remove(product)
    return redirect('carts:cart')

def clear(request):
    cart = get_or_create_cart(request)
    cart.products.clear()
    return redirect('carts:cart')
