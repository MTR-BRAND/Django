# products/urls.py

from django.urls import path
from .views import product_list  # Use the correct function name

urlpatterns = [
    path('', product_list, name='products_list'),  # Adjusted to use product_list
]
