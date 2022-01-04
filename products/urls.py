from django.urls import path
from products.views import show_all_products, product_details


app_name = 'products'

urlpatterns = [
    path('', show_all_products, name='all'),
    path('<product_id>/', product_details, name='details'),

]
