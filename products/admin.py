from django.contrib import admin
from products.models import Product, Category
from notifications.utils import create_notification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'category', 'price', 'quantity']

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        create_notification(obj, 'new_product')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
