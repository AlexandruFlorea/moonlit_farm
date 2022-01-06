from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product


def show_all_products(request):
    products = Product.objects.all()

    return render(request, 'products/products.html', {
        'products': products,
    })


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    return render(request, 'products/details.html', {
        'product': product
    })
