from django.db.models.query_utils import Q
from products.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.contrib.auth.decorators import user_passes_test
from .forms import NewProductForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from categories.models import Category

# Create your views here.

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    
    # Esto es una negrada pero funciona
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Productos'
        context['cards'] = self.queryset[:3]         
        context['list'] = self.queryset[3:]
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  

class ProductSearchListView(ListView):
    template_name = 'products/search.html' 
    def get_queryset(self):
        filters = Q(title__icontains=self.query()) | Q(category__title__icontains=self.query())
        return Product.objects.filter(filters)
    def query(self):
        return self.request.GET.get('q')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query 
        context['count'] = context['product_list'].count()
        return context

@user_passes_test(lambda user: user.is_superuser)
def new(request):
    form = NewProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        title = form.data.get('title')
        description = form.data.get('description')
        price = form.data.get('price')
        cat_id = form.data.get('category')
        product = Product(title=title, image=request.FILES['image'], description=description, price=price)
        product.save()
        if cat_id:
            category = get_object_or_404(Category, id=cat_id)
            category.save()
            category.products.add(product)
        if product:
            messages.success(request, 'Producto agregado exitosamente')
            return redirect('index')
    return render(request, 'products/new.html',{
        'form':form ,
        'title': 'Nuevo Producto'
    })

@user_passes_test(lambda user: user.is_superuser)
def edit(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = NewProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        product.title = form.data.get('title')
        product.description = form.data.get('description')
        product.price = form.data.get('price')
        cat_id = form.data.get('category')
        product.image = request.FILES['image']
        product.save()
        if cat_id:
            category = get_object_or_404(Category, id=cat_id)
            category.save()
            category.products.add(product)
        if product:
            messages.success(request, 'Producto editado exitosamente')
            return redirect('index')
    return render(request, 'products/new.html',{
    'form':form ,
    'title': 'Actualizar Producto'
    })   

@user_passes_test(lambda user: user.is_superuser)
def delete(request, slug):
    product = get_object_or_404(Product, slug=slug)
    product.delete()
    return redirect('index')