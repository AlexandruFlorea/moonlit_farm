from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def show_all_products(request):
    return render(request, 'products/products.html', {})


def product_details(request, product_id):
    product = get_object_or_404(Product, product_id)

    return render(request, 'products/details.html', {
        'product': product
    })
