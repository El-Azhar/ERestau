from django.contrib import admin

# Register your models here.
from core.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'quantity', 'status']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)