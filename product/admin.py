from django.contrib import admin
from .models import Product

# Data display en Django Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "brand", "type", "stock", "price"]
    list_filter = ["name", "brand", "price"]