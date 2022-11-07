from django.contrib import admin
from .models import Category, Product


admin.site.register(Category)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']