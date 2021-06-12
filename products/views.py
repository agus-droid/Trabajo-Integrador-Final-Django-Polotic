from django.db.models.query_utils import Q
from products.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product

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