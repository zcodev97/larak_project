from django.contrib import admin

from .models import Product, Size, \
    Categorie, Order, OrderStatus


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['id','image' ,  'title', 'description', 'size','amount', 'created_at', 'created_by']


@admin.register(Size)
class Size(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Categorie)
class Categorie(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(OrderStatus)
class OrderStatus(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'created_at']
