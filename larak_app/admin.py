import json

from django.contrib import admin
from django.utils.html import format_html

from .models import Product, Category, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price:,.0f}")

    def formatted_cost_dinar(self, obj):
        return format_html(f"IQD {obj.cost:,.0f}")

    formatted_price_dinar.short_description = 'Price'  # Sets the column header
    formatted_cost_dinar.short_description = 'Cost'  # Sets the column header

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('title', 'category__title')  # Fields to search by

    def get_actions(self, request):
        actions = super(ProductAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    list_display = [
        # 'id',
        'title',
        'image',
        'category', 'amount',
        'formatted_price_dinar', 'formatted_cost_dinar', 'profit', 'discount', 'created_at', 'on_home_screen','on_banner',
        'created_by']
    fields = ('image', 'title', 'description', 'category', 'amount', 'price', 'cost', 'discount', 'on_home_screen','on_banner')

    def save_model(self, request, obj, form, change):
        if not change:  # Check if the object is being created
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        # 'id',
        'title', 'on_home_screen', 'created_at', 'created_by']

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('title',)  # Fields to search by

    def get_actions(self, request):
        actions = super(CategoryAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ['client', 'cart', 'status']

    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    list_display = [
        # 'id',
        'client', 'created_at']

    # def formatted_cart(self, obj):
    #     # Format the JSON data with indentation for better readability
    #     formatted_data = json.dumps(obj.cart, indent=2)
    #     # Use format_html to safely render the formatted JSON in the Django admin
    #     return format_html('<pre>{}</pre>', formatted_data)
    #
    # formatted_cart.short_description = 'Cart (Formatted)'  # Set the column header


    # def formatted_status(self, obj):
    #     # Format the JSON data with indentation for better readability
    #     formatted_data = json.dumps(obj.status, indent=2)
    #     # Use format_html to safely render the formatted JSON in the Django admin
    #     return format_html('<pre>{}</pre>', formatted_data)
    #
    # formatted_status.short_description = 'Status (Formatted)'  # Set the column header

    # def get_actions(self, request):
    #     actions = super(OrderAdmin, self).get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
    #
