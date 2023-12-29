from django.contrib import admin

from .models import Product, Categorie, Order, Invoice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'description', 'category', 'amount', 'price', 'cost', 'created_at',
                    'created_by']
    fields = ('image', 'title', 'description', 'category', 'amount', 'price', 'cost', 'created_at')

    def save_model(self, request, obj, form, change):
        if not change:  # Check if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Categorie)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'product', 'price', 'amount', 'status', 'created_at']


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_id','client', 'product', 'price', 'amount', 'status', 'created_at']

