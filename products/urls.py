from django.urls import path
from products.views import ProductListView, ProductDetailView, add_product_to_cart, show_checkout, remove_product_from_cart


app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='all'),
    path('<int:pk>/', ProductDetailView.as_view(), name='details'),
    path('<int:product_id>/add_to_cart/', add_product_to_cart, name='add_to_cart'),
    path('checkout/', show_checkout, name='checkout'),
    path('<int:product_id>/remove_from_cart/', remove_product_from_cart, name='remove_from_cart'),
]
