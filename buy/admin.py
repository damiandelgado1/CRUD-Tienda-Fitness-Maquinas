from django.contrib import admin
from .models import Buy

# Data display en Django Admin
@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = ["client", "product"]
    list_filter = ["client"]