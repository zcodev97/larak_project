from django.contrib import admin

from .models import Product, Categorie, Order


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'description', 'category', 'amount', 'price', 'cost', 'created_at',
                    'created_by']
    fields = ('image', 'title', 'description', 'category', 'amount', 'price', 'cost', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:  # Check if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Categorie)
class Categorie(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', 'created_at']
