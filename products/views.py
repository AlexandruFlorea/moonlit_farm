from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.contrib import messages
from products.models import Product
from utils.cart import Cart


class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 4
    ordering = 'id'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/details.html'


def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(product_id, quantity)
    messages.success(request, f'{quantity} {product.name} added to cart.')

    return redirect(reverse('products:all'))


def show_checkout(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = [
        {
            'product': product,
            'quantity': cart[str(product.id)],
            'total': "%.2f" % (float(product.price) * int(cart[str(product.id)]))
        }
        for product in products
    ]

    return render(request, 'products/checkout.html', {
        'cart_items': cart_items,
        'cart': cart,
    })


def remove_product_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)
    cart.remove(product_id)

    return redirect(reverse('products:checkout'))
