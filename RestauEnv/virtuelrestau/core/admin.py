from django.contrib import admin

# Register your models here.
from core.models import Category, Product, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'status']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name',  'selected_product', 'phone_number', 'status', 'created_at', 'order_id']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)