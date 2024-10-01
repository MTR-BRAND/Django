from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()  # Corrected this line
    return render(request, 'products/product_list.html', {'products': products})
